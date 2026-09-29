import re
import frappe
from frappe.utils import cint, getdate

TO_DATE_PATTERN = re.compile(r"(?<![`:\w])(?<!%\()(?<!%\b)\bto_date\b(?![\(`])", re.IGNORECASE)

def custom_validate_leave_overlap(self):
	if not self.name:
		# hack! if name is null, it could cause problems with !=
		self.name = "New Leave Application"

	for d in frappe.db.sql(
		"""
		select
			name, leave_type, posting_date, `from_date`, `to_date`, total_leave_days, half_day, half_day_date
		from `tabLeave Application`
		where employee = %(employee)s and docstatus < 2 and status in ('Open', 'Approved')
		and `to_date` >= %(from_date)s and `from_date` <= %(to_date)s
		and name != %(name)s""",
		{
			"employee": self.employee,
			"from_date": self.from_date,
			"to_date": self.to_date,
			"name": self.name,
		},
		as_dict=1,
	):
		if (
			cint(self.half_day) == 1
			and cint(d.half_day) == 1
			and getdate(self.half_day_date) == getdate(d.half_day_date)
		):
			total_leaves_on_half_day = self.get_total_leaves_on_half_day()
			if total_leaves_on_half_day >= 1:
				self.throw_overlap_error(d)
		else:
			self.throw_overlap_error(d)


def custom_get_leave_entries(employee, leave_type, from_date, to_date):
	"""Returns leave entries between from_date and to_date with MariaDB 12 compatible backticked column names."""
	return frappe.db.sql(
		"""
		SELECT
			employee, leave_type, `from_date`, `to_date`, leaves, transaction_name, transaction_type, holiday_list,
			is_carry_forward, is_expired
		FROM `tabLeave Ledger Entry`
		WHERE employee=%(employee)s AND leave_type=%(leave_type)s
			AND docstatus=1
			AND (leaves<0
				OR is_expired=1)
			AND (`from_date` between %(from_date)s AND %(to_date)s
				OR `to_date` between %(from_date)s AND %(to_date)s
				OR (`from_date` < %(from_date)s AND `to_date` > %(to_date)s))
	""",
		{"from_date": from_date, "to_date": to_date, "employee": employee, "leave_type": leave_type},
		as_dict=1,
	)


try:
	from hrms.hr.doctype.leave_application.leave_application import LeaveApplication
	class CustomLeaveApplication(LeaveApplication):
		validate_leave_overlap = custom_validate_leave_overlap
except Exception:
	class CustomLeaveApplication:
		pass


_patched = False

def patch_all():
	global _patched
	if _patched:
		return
	_patched = True

	# 1. Patch LeaveApplication class and module function in HRMS
	try:
		import hrms.hr.doctype.leave_application.leave_application as la_mod
		la_mod.LeaveApplication.validate_leave_overlap = custom_validate_leave_overlap
		la_mod.get_leave_entries = custom_get_leave_entries
	except Exception:
		pass

	# 2. Patch Database.sql globally so ANY query with unquoted to_date column is safe in MariaDB 12
	try:
		import frappe.database.database as db_mod

		if not getattr(db_mod.Database, "_hrmsapp_to_date_patched", False):
			orig_sql = db_mod.Database.sql

			def safe_sql(self, query, *args, **kwargs):
				if isinstance(query, str) and "to_date" in query.lower():
					query = TO_DATE_PATTERN.sub("`to_date`", query)
				return orig_sql(self, query, *args, **kwargs)

			db_mod.Database.sql = safe_sql
			db_mod.Database._hrmsapp_to_date_patched = True
	except Exception:
		pass

	# 3. Patch Database._transform_query as a secondary defense layer
	try:
		import frappe.database.database as db_mod

		if not getattr(db_mod.Database, "_hrmsapp_transform_patched", False):
			orig_transform = db_mod.Database._transform_query

			def safe_transform_query(self, query, values):
				query, values = orig_transform(self, query, values)
				if isinstance(query, str) and "to_date" in query.lower():
					query = TO_DATE_PATTERN.sub("`to_date`", query)
				return query, values

			db_mod.Database._transform_query = safe_transform_query
			db_mod.Database._hrmsapp_transform_patched = True
	except Exception:
		pass


patch_all()
