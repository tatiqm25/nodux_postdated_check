# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json
from frappe import _, scrub, ValidationError
from frappe.utils import flt, comma_or, nowdate
from erpnext.accounts.utils import get_outstanding_invoices, get_account_currency, get_balance_on
from erpnext.accounts.party import get_party_account
from erpnext.accounts.doctype.journal_entry.journal_entry \
	import get_average_exchange_rate, get_default_bank_cash_account
from erpnext.setup.utils import get_exchange_rate
from erpnext.accounts.general_ledger import make_gl_entries

from erpnext.controllers.accounts_controller import AccountsController

def create_posdated_check(doc, event):
	if doc.docstatus == 0:
		check = False
		for line in doc.payments_type:
			account_types = ["Bank"]
			account_type = frappe.db.get_value("Account", line.account, "account_type")
			if (account_type in account_types) and (doc.payment_type == "Receive"):
				check = True
		if check == True:
			postdated_check = frappe.get_doc({
				"doctype":"Postdated Check",
				"customer": doc.party,
				"customer_name":doc.party_name,
				"date": nowdate()
			})
			for line in doc.payments_type:
				linep = frappe.get_doc({
					"doctype": "Postdated Check Line",
					"number": doc.naming_series,
					"due_date": line.date_reference,
					"date": nowdate(),
					"amount": line.amount,
					"from_account": line.account
				})
				postdated_check.append('postdated_check_lines', linep)

			#postdated_check.docstatus = 1
			postdated_check.save()
