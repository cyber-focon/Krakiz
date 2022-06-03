import KrakizAPI as API
import functions
import time
import os
#OTE0MTIxMTExOTMzOTQzODc5.GL5QRn.gtF8aWswlIxuR4HcE6nsyLCtkkW3g2O0cZUFvI

utils = API.Utils
client = API.Client

def main():
	bot = API.Bot(client.getData()["token"])
	comment = "Krakiz as been lauch"
	while True:
		functions.clear()
		functions.printBanner()
		opt = input(functions.getPrompt(comment))

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
		else:
			comment = f"\"{opt}\" is not an options"

if __name__ == '__main__':
	functions.clear()

	if client.isValiedData():
		main()
	else:
		t = input("\033[96m┌──[\033[95mToken\033[96m]───╼ \033[95m")
		b = input("\033[96m├──[\033[95mBot Id\033[96m]──╼ \033[95m")
		u = input("\033[96m└──[\033[95mUser Id\033[96m]─╼ \033[95m")

		client.initData(t, b, u)
		main()