import frappe
from frappe.utils import cint, getdate
from hrms.hr.doctype.leave_application.leave_application import LeaveApplication

class CustomLeaveApplication(LeaveApplication):
	def validate_leave_overlap(self):
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
