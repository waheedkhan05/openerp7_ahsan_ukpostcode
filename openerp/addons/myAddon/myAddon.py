from openerp.osv import fields, osv
class student_info(osv.osv):
  _name = 'student.info'
  _columns = {
		'name': fields.char('Name',size=20, required=True),
		'roll_no': fields.integer('Roll No:',required=True)
		}
student_info()
