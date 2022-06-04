import json
import os

class Client:
	def initData(token, userId, botId):
		try:
			z = file.open(os.path.expanduser('~')+"/.krakiz/data.json", "w+")
		except:
			os.makedirs(os.path.expanduser('~')+"/.krakiz", exist_ok=True)
		with open(os.path.expanduser('~')+"/.krakiz/data.json", "w+") as f:
			data = {
				"token": token,
				"userId": userId,
				"botId": botId
			}
			json.dump(data, f)

	def isValiedData():
		try:
			with open(os.path.expanduser('~')+"/.krakiz/data.json", "r") as f:
				data = json.load(f)
				if "token" in data and "userId" in data and "botId" in data:
					return True
				return False
		except:
			return False

	def getData():
		if Client.isValiedData():
			with open(os.path.expanduser('~')+"/.krakiz/data.json", "r") as f:
				return json.load(f)
		return None