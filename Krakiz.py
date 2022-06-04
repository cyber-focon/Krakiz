import KrakizAPI as API
import functions
import time
import os

utils = API.Utils
client = API.Client

def main():
	bot = API.Bot(client.getData()["token"])
	comment = "Krakiz as been lauch"
	while True:
		functions.clear()
		functions.printBanner()
		opt = input(functions.getPrompt(comment))

		try:
			if opt == "1":
				guildId = input("\033[96m└──[\033[95mGuild Id\033[96m]───╼ \033[95m")
				count = input("\033[96m└──[\033[95mCount\033[96m]──────╼ \033[95m")
				if count != "MAX":
					try:
						count = int(count)
					except:
						comment = f"\"{count}\" is not an number"
						continue
					if 500 - utils.getChannelCount(bot, guildId, 500) < count:
						count = 500 - utils.getChannelCount(bot, guildId, 500)
				else:
					count = 500 - utils.getChannelCount(bot, guildId, 500)
				name = input("\033[96m└──[\033[95mName\033[96m]───────╼ \033[95m")
				bot.createChannels(guildId, name, count)
				comment = f"{count} channels are been create"
			elif opt == "2":
				guildId = input("\033[96m└──[\033[95mGuild Id\033[96m]───╼ \033[95m")
				count = input("\033[96m└──[\033[95mCount\033[96m]──────╼ \033[95m")
				if count != "MAX":
					try:
						count = int(count)
					except:
						comment = f"\"{count}\" is not an number"
						continue
					if 250 - utils.getRoleCount(bot, guildId, 250) < count:
						count = 250 - utils.getRoleCount(bot, guildId, 250)
				else:
					count = 250 - utils.getRoleCount(bot, guildId, 250)
				name = input("\033[96m└──[\033[95mName\033[96m]───────╼ \033[95m")
				bot.createRoles(guildId, name, count)
				comment = f"{count} roles are been create"
			elif opt == "3":
				channelId = input("\033[96m└──[\033[95mChannel Id\033[96m]───╼ \033[95m")
				if channelId != "ALL":
					bot.deleteChannel(channelId)
					comment = "The channel as been deleted"
				else:
					guildId = input("\033[96m└──[\033[95mGuild Id\033[96m]─────╼ \033[95m")
					bot.deleteAllChannels(guildId)
					comment = "All channel are been deleted"
			elif opt == "4":
				guildId = input("\033[96m└──[\033[95mGuild Id\033[96m]─────╼ \033[95m")
				roleId = input("\033[96m└──[\033[95mRole Id\033[96m]──────╼ \033[95m")
				if roleId != "ALL":
					bot.deleteRole(guildId, roleId)
					comment = "The roles as been deleted"
				else:
					bot.deleteAllRoles(guildId)
					comment = "All roles are been deleted"
			elif opt == "5":
				channelId = input("\033[96m└──[\033[95mChannel Id\033[96m]───╼ \033[95m")
				message = input("\033[96m└──[\033[95mMessage\033[96m]──────╼ \033[95m")
				bot.sendMessage(channelId, message)
				comment = "The message as been send"
			elif opt == "6":
				message = input("\033[96m└──[\033[95mMessage\033[96m]──────╼ \033[95m")
				channelId = input("\033[96m└──[\033[95mChannel Id\033[96m]───╼ \033[95m")
				if channelId != "ALL":
					bot.spamMessageInTheChannel(channelId, message)
					comment = "The channel is being spammed"
				else:
					guildId = input("\033[96m└──[\033[95mGuild Id\033[96m]─────╼ \033[95m")
					bot.spamAllChannels(guildId, message)
					comment = "All channels are being spammed"
			elif opt == "7":
				guildId = input("\033[96m└──[\033[95mGuild Id\033[96m]─────╼ \033[95m")
				memberId = input("\033[96m└──[\033[95mMember Id\033[96m]────╼ \033[95m")
				if memberId != "ALL":
					bot.kickMember(guildId, memberId)
					comment = "The member as been kicked"
				else:
					bot.kickAllMember(guildId)
					comment = "All members are been kicked"
			elif opt == "8":
				guildId = input("\033[96m└──[\033[95mGuild Id\033[96m]─────╼ \033[95m")
				memberId = input("\033[96m└──[\033[95mMember Id\033[96m]────╼ \033[95m")
				if memberId != "ALL":
					bot.banMember(guildId, memberId)
					comment = "The member as been baned"
				else:
					bot.banAllMember(guildId)
					comment = "All members are been baned"
			elif opt == "t":
				functions.initData()
				bot = API.Bot(client.getData()["token"])
			elif opt == "i":
				functions.printInvitePanel()
				input("")
			elif opt == "c":
				bot.clearTask()
				comment = "All task as been cleared"
			elif opt == "x":
				bot.clearTask()
				functions.clear()
				return
			else:
				comment = f"\"{opt}\" is not an options"
		except KeyboardInterrupt:
			continue

if __name__ == '__main__':
	if not client.isValiedData():
		functions.initData()
	main()