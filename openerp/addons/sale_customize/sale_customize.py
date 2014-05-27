from osv import fields, osv
import time

class sale_order(osv.osv):
	_inherit = "sale.order"
	_description = "Extending sale.order to add Fields like Make,OS,Fault,Username,Password etc"
	_columns = {
		'x_equipusername':fields.char('Username',size=50),
		'x_equippass':fields.char('Password',size=50),
		'x_equipos':fields.char('OS',size=128),
		'x_equiptype':fields.many2one('product.product','Type'),
		'x_equipfault':fields.char('Fault'),
		'x_equipmake':fields.char('Make'),
		'x_equipserial':fields.char('Serial'),
		'x_equipaccessories':fields.char('Accessories'),
	}
sale_order()