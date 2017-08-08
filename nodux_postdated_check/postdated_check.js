// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
// frappe.ui.form.on('Postdated Check', {
//
// 	terceros_name: function(frm) {
// 		var total_amount = 0.0;
// 		$.each(frm.doc.payments_type || [], function(i, row) {
// 				if (row.amount) {
// 				total_amount += flt(row.amount);
// 			}
// 		});
// 		frm.set_value("paid_amount", total_amount);
// 	},
//
// 	date_reference:function(frm){
// 		var date_ref;
// 		$.each(frm.doc.payments_type || [], function(i, row) {
// 				if (row.date_reference) {
// 					date_ref = row.date_reference;
// 			}
// 		});
// 		frm.set_value("reference_date", date_ref);
// 	}
//
// })
