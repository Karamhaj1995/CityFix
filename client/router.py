from client.handlers.starter import MainHandler, LoginHandler, RegisterHandler
from client.handlers.profile import ProfileHandler
from client.handlers.users import Api as UserAPI
from client.handlers.hazards import Api as HazardsAPI
urls = [
		# web-pagging
		(r"/", MainHandler),
		(r"/login", LoginHandler),
		(r"/register", RegisterHandler),
		(r"/profile", ProfileHandler),
		# api-routing
		(r"/api/v1/users", UserAPI),
		(r"/api/v1/hazards", HazardsAPI)
	]