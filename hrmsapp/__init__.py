__version__ = "0.0.1"

# Apply runtime compatibility patches (e.g. MariaDB 12 TO_DATE reserved keyword fix)
try:
	from hrmsapp.overrides import patch_all
	patch_all()
except Exception:
	pass
