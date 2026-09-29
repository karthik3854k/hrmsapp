import os
import frappe
from frappe.boot import load_translations

no_cache = 1


def get_context(context):
	csrf_token = frappe.sessions.get_csrf_token()
	frappe.db.commit()  # nosempgrep
	context = frappe._dict()
	context.csrf_token = csrf_token
	context.boot = get_boot()
	context.site_name = frappe.local.site
	context.base_template = None

	# Dynamically load the compiled index.html directly from public/frontend
	# This ensures hrms always serves whatever current build hash exists on disk,
	# permanently eliminating 404 blank screens from stale static templates.
	index_path = frappe.get_app_path("hrmsapp", "public", "frontend", "index.html")
	if os.path.exists(index_path):
		try:
			with open(index_path, "r", encoding="utf-8") as f:
				raw_html = f.read()
			context.app_html = frappe.render_template(raw_html, context)
		except Exception:
			frappe.log_error("Failed to render hrmsapp public frontend index.html")
			context.app_html = None
	else:
		context.app_html = None

	return context


@frappe.whitelist(methods=["POST"], allow_guest=True)
def get_context_for_dev():
	if not frappe.conf.developer_mode:
		frappe.throw(frappe._("This method is only meant for developer mode"))
	return get_boot()


def get_boot():
	bootinfo = frappe._dict(
		{
			"site_name": frappe.local.site,
			"push_relay_server_url": frappe.conf.get("push_relay_server_url") or "",
			"default_route": get_default_route(),
		}
	)

	bootinfo.lang = frappe.local.lang
	load_translations(bootinfo)

	return bootinfo


def get_default_route():
	return "/hrms"
