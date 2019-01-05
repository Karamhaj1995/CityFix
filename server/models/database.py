from server.const.db_conf import db_config
import os
import datetime
from mongoengine import *
from mongoengine import signals
from hashlib import sha512
from bson import json_util
import json

def connect_to_database():
	print('Connecting to database...(%s %s %s)' % (db_config['connection'],db_config['port'],db_config['dbname']))
	try:
		connect(db_config['dbname'], host=db_config['connection'], port=int(db_config['port']),username=db_config['dbusername'],password=db_config['dbpassword'])
	except:
		print("Unable to connect.")
	print("Connect to database was successful.")

connect_to_database()

class User(Document):
	name = StringField(required=True)
	password = StringField(required=True)
	salt_key = 'rWxHp4CBC8h0SiPY3gPKIGbed14bBCsj0VK8RQrrmKqa0ZveQvXNd7MI2twENvVJHq7vdYJHWPhLq5ONA8nr6bbZenANIrynBUEVbMHpMud3K8iUSAanfKTZ'
	meta = {'collection': 'Users'}
	
	def check_user_pass(self, password):
		try:
			hash_password, salt = self.password.split(':')
			result = hash_password == sha512(salt.encode() + password.encode()).hexdigest()
			return result
		except Exception as e:
			print(e)
			return False

	def change_password(self, password):
		self.password = sha512(self.salt_key.encode()+password.encode()).hexdigest() + ':' + self.salt_key

class Hazard(Document):
	title = StringField()
	description = StringField()
	location = ReferenceField('Location')
	datetime = DateTimeField(default=datetime.datetime.now())
	lat = StringField()
	lng = StringField() 
	user = ReferenceField('User')
	meta = {'collection': 'Hazards'}

class Location(Document):
	Lat = StringField(required=True)
	Lng = StringField(required=True)
	FullAddress = StringField(default='')
	meta = {'collection': 'Locations'}
