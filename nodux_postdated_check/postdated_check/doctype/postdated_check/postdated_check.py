# -*- coding: utf-8 -*-
# Copyright (c) 2015, NODUX and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class PostdatedCheck(Document):
	def generate_deposit(self):
		for line in self.postdated_check_lines:
			if line.account_bank:
				lined = frappe.get_doc({
					"doctype": "Journal Entry Account",
					"account": line.account_bank,
					"debit_in_account_currency":line.amount,
					"credit_in_account_currency":0,
				})
				linec = frappe.get_doc({
					"doctype": "Journal Entry Account",
					"account": line.from_account,
					"debit_in_account_currency":0,
					"credit_in_account_currency":line.amount
				})
				journal = frappe.get_doc({
					"doctype":"Journal Entry",
					"voucher_type": "Journal Entry",
					"posting_date": nowdate(),
				})

				journal.append('accounts', lined)
				journal.append('accounts', linec)
				journal.save()
				journal.docstatus = 1
				journal.save()
				self.status = "Done"
				self.save()
			else:
				frappe.throw("Ingrese la cuenta de banco de depósito")
