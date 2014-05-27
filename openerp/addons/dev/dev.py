from osv import fields, osv

class dev_person(osv.osv):
    _name = "dev.person"
    _description = "Person is testing module built for learning about OpenERP"
    _columns = {
        'person_name': fields.char('Name', size=128, required=True, help="This is the name of the person"),
	'age':fields.integer('Age',required=True),
	'date_of_joining':fields.date('Date of Joining'),
	'description':fields.text("Description"),
    }
dev_person()
