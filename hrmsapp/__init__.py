__version__ = "0.0.1"

import re

def _patch_mariadb_to_date_support():
	try:
		from frappe.database.mariadb.database import MariaDBDatabase

		if getattr(MariaDBDatabase, "_hrms_to_date_patched", False):
			return

		_orig_transform_query = MariaDBDatabase._transform_query
		_to_date_pattern = re.compile(r"(?<![`%:\.\w(])to_date(?![\(`%:\w)])", re.IGNORECASE)

		def _safe_transform_query(self, query, values):
			query, values = _orig_transform_query(self, query, values)
			if isinstance(query, str) and "to_date" in query.lower():
				query = _to_date_pattern.sub("`to_date`", query)
			return query, values

		MariaDBDatabase._transform_query = _safe_transform_query
		MariaDBDatabase._hrms_to_date_patched = True
	except Exception:
		pass

_patch_mariadb_to_date_support()
