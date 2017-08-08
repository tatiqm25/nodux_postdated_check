// Copyright (c) 2016, NODUX and contributors
// For license information, please see license.txt

frappe.ui.form.on('Postdated Check', {
	refresh: function(frm) {
		if (frm.doc.status== 'Draft') {
			frm.add_custom_button(__("Depositar"), function() {
				frm.events.generate_deposit(frm);
			}).addClass("btn-primary");
		}
		frm.refresh_fields();
	},

	generate_deposit: function(frm) {
		return frappe.call({
			doc: frm.doc,
			method: "generate_deposit",
			freeze: true,
			callback: function(r) {
				frm.refresh_fields();
				frm.refresh();
			}
		})
		frm.refresh_fields();
		frm.refresh();
	}
});
