import requests
import json

class Utils:
	def getCrateChannelData(channelName):
		return {"name": channelName, "type": 0}

	def getCrateRoleData(roleName):
		return {"name": roleName}

	def getMessageData(message):
		return {"content": message}

	def getMemberCount(bot, guildId):
		r = requests.get(f'https://discord.com/api/v9/guilds/{guildId}/members?limit=1000', headers=bot.header)
		rjson = json.loads(r.text)
		return len(rjson)

	def getChannelCount(bot, guildId, limit):
		r = requests.get(f'https://discord.com/api/v9/guilds/{guildId}/channels?limit={limit}', headers=bot.header)
		rjson = json.loads(r.text)
		return len(rjson)

	def getRoleCount(bot, roleId, limit):
		r = requests.get(f'https://discord.com/api/v9/guilds/{roleId}/roles?limit={limit}', headers=bot.header)
		rjson = json.loads(r.text)
		return len(rjson)

	def getIdOfAllMember(bot, guildId):
		r = requests.get(f'https://discord.com/api/v9/guilds/{guildId}/members?limit=1000', headers=bot.header)
		rjson = json.loads(r.text)
		members = []
		for i in range(len(rjson) - 1):
			members.append(rjson[i]["user"]["id"])
		return members

	def getIdOfAllChannel(bot, guildId, limit):
		r = requests.get(f'https://discord.com/api/v9/guilds/{guildId}/channels?limit={limit}', headers=bot.header)
		rjson = json.loads(r.text)
		channels = []
		for i in range(len(rjson)):
			channels.append(rjson[i]["id"])
		return channels

	def getIdOfAllRole(bot, roleId, limit):
		r = requests.get(f'https://discord.com/api/v9/guilds/{roleId}/roles?limit={limit}', headers=bot.header)
		rjson = json.loads(r.text)
		roles = []
		for i in range(len(rjson)):
			roles.append(rjson[i]["id"])
		return roles

	def getInvite(botId, permission):
		return f"https://discord.com/api/oauth2/authorize?client_id={botId}&permissions={permission}&scope=bot"

	def getAdminInvite(botId):
		return Utils.getInvite(botId, 8)

	def getRestrainInvite(botId):
		return Utils.getInvite(botId, 268438550)