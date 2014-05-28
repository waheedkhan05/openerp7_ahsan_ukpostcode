from osv import fields, osv
import time


class res_partner(osv.osv):	

	_inherit = "res.partner"
	_description = "Extending Customer Information to add Post Code Information"

	def populate_postcode_dropdown(self, cr, uid,context=None):
		try:
			to_return = self.pool.get('uk_postcodes').getAllPostCodes(cr,uid)
			return to_return
		except:
			return [('Post Codes Unavailable','Post Codes Unavailable')]

	_columns = {
		'zip' : fields.many2one('uk_postcodes',domain="[('zip','=',name)]"),
		'state_id':fields.many2one('uk_postcodes',domain="[('state_id','=',name)]")
	}

	def onchange_postcode(self, cr, uid,ids,postcode, context=None):
		if postcode:
			obj = self.pool.get('uk_postcodes').getTownCountyWithPostcode(cr,uid,postcode,context)
			if obj:
				return {
		        'value': {
		            'street2': obj['town'],
		            'state_id': obj['state_id'],
		            'country_id':233
				         }
				    }
		return {}

	def onchange_County(self, cr, uid,ids, context=None):
		if ids:
			obj = self.pool.get('uk_postcodes').getAllCounties(cr,uid,ids,context)
		return {}


res_partner()

class uk_postcodes(osv.osv):
	_name = "uk_postcodes"
	_description = "Extending Customer Information to add Post Code Information"
	_columns = {
		'zip':fields.char('Post Code',size=5),
		'x':fields.integer(),
		'y':fields.integer(),
		'latitude':fields.float('Latitude',digits=(5,2)),
		'longitude':fields.char('Longitude',size=8),
		'town':fields.char('Town',size=255),
		'state_id':fields.char('County',size=255),
	}

	def name_search(self, cr, uid, name='', args=None, operator='ilike',context=None, limit=100):
	    ids = []
	    if not args:
	        args = []
	    else:
	    	if 'state_id' in args[0]:
	    		ids = self.search(cr, uid, [('state_id',operator,name)],limit=limit, context=context)
	    		return [(r.id,r.state_id) for r in self.browse(cr, uid, ids, context)]
	    	elif 'zip' in args[0]:
	    		ids = self.search(cr, uid, [('zip',operator,name)],limit=limit, context=context)
	    		return [(r.id,r.zip) for r in self.browse(cr, uid, ids, context)]
	    	else:
			    print 'name_search name:%s args:%s,context:%s'%(name,args,context)
			    print name
		return []
	    
	    #return self.name_get(cr, uid, ids, context)

	# def name_get(self,cr, uid, ids, context):
	# 	#return (self.browse(cr,uid,ids)[0].id,self.browse(cr,uid,ids)[0].postcode)
	# 	res = []
	# 	for r in self.read(cr,uid,ids):
	# 		res.append((r['id'],r['zip']))
	# 	return res

	def getTownCountyWithPostcode(self,cr,uid,post,context):
		postcode_id = self.search(cr, uid, [('id','=',post)], context=context)
		obj = self.browse(cr,uid,postcode_id)
		print dir(obj[0])
		if obj != None:
			return {'town':obj[0].town,'state_id':obj[0]._id}

	def getAllPostCodes(self,cr,uid,context=None):
		all_record_ids = self.search(cr, uid,[])
		all_records = self.browse(cr,uid,all_record_ids)
		return [(r.id,r.zip) for r in all_records]

	def getPostCodes(self,cr,uid,post,context=None):
		all_record_ids = search(cr, uid, [('id','=',post)], context=context)
		all_records = self.browse(cr,uid,all_record_ids)
		return [(r.id,r.zip) for r in all_records]

	def getCounty(self,cr,uid,post,context=None):
		all_record_ids = search(cr, uid, [('id','=',post)], context=context)
		all_records = self.browse(cr,uid,all_record_ids)
		return [(r.id,r.state_id) for r in all_records]

	def getAllCounties(self,cr,uid,context=None):
		all_record_ids = self.search(cr, uid,[])
		all_records = self.browse(cr,uid,all_record_ids)
		return [(r.id,r.state_id) for r in all_records]

	_default = {
		'x':0,
		'y':0,
		'latitude':0.00,
		'longitude':'0',
	}