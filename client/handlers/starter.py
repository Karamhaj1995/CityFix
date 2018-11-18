import tornado.web
import tornado.ioloop
from server.models.database import User
from server.models.users import User as UserManager
from server.models.hazards import Hazard as HazardManager

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		parameters = {}
		parameters['latest_hazards'] = HazardManager().hazards()
		for hazard in parameters['latest_hazards']:
			hazard['lat'] = hazard['location']['Lat']
			hazard['lng'] = hazard['location']['Lng']
		self.render("index.html", parameters=parameters)

class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("login.html", parameters={"Name":"Karam"})

	def post(self):
		self.render("asd.html", parameters={"Name":"Karam"})

class RegisterHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("register.html")