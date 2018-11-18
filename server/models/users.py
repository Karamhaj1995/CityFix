import jwt,time
from server.models.database import User as UserDB

class User():

	def users(self):
		return UserDB.objects()

	def user_by_name(self, name):
		return UserDB.objects(name=name)

	def create_user(self, username, password):
		try:
			user = UserDB(name=username, password=password)
			user.commit(True)
			return user.to_json()
		except:
			return False

	def delete_user(self, id):
		user = UserDB(pk=id)
		user.delete()
		return UserDB.objects()

	def check_login(self, data):
		print(data)
		user = UserDB.objects(name=data['username'], password=data['password']).first()
		if user is None:
			return False
		else:
			return user.to_json()

	def set_user_token(self, username,password):
		user = UserDB.objects(name=username).first()
		if user is None:
			return False
		if not user.Status:
			return False
		if user.check_user_pass(password):
			payload = {
				'username': user['name'],
				'_id': user['_id']
			}
			return jwt.encode(payload, 'rWxHp4CBC8h0SiPY3gPKIGbed14bBCsj0VK8RQrrmKqa0ZveQvXNd7MI2twENvVJHq7vdYJHWPhLq5ONA8nr6bbZenANIrynBUEVbMHpMud3K8iUSAanfKTZ', algorithm='HS256')
		else:
			return False