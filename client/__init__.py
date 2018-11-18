import tornado.web

class CityFixReq(tornado.web.RequestHandler):
	
	token = {}

	def initialize(self):
		pass

	def get_current_user(self):
		pass

	def api_response(self, results, **kwargs):
		pass