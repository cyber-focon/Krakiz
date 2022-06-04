import KrakizAPI as API
import platform
import os

client = API.Client

banner = """\033[96m
		   ██╗  ██╗██████╗  █████╗ ██╗  ██╗██╗███████╗
		   ██║ ██╔╝██╔══██╗██╔══██╗██║ ██╔╝██║╚════██║
		   █████═╝ ██████╔╝███████║█████═╝ ██║  ███╔═╝
		   ██╔═██╗ ██╔══██╗██╔══██║██╔═██╗ ██║██╔══╝
		   ██║ ╚██╗██║  ██║██║  ██║██║ ╚██╗██║███████╗
		   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝

	┌────────────────────┬────────────────────┬────────────────────┐
	│\033[95m[\033[96m1\033[95m] Create Channels \033[96m│\033[95m[\033[96m5\033[95m] Send message    \033[96m│\033[95m[\033[96mt\033[95m] Change Token    \033[96m│
	│\033[95m[\033[96m2\033[95m] Create Role     \033[96m│\033[95m[\033[96m6\033[95m] Spam message    \033[96m│\033[95m[\033[96mi\033[95m] Invite          \033[96m│
	│\033[95m[\033[96m3\033[95m] Delete Channels \033[96m│\033[95m[\033[96m7\033[95m] Kick members    \033[96m│\033[95m[\033[96mc\033[95m] Clear           \033[96m│
	│\033[95m[\033[96m4\033[95m] Delete Role     \033[96m│\033[95m[\033[96m8\033[95m] Ban members     \033[96m│\033[95m[\033[96mx\033[95m] Exit            \033[96m│
	└────────────────────┴────────────────────┴────────────────────┘
	"""

def clear():
	if (platform.system() == "Windows"):
		os.system("cls")
	else:
		os.system("clear")

def getPrompt(info):
	return f"\033[96m┌─[\033[95mchoise\033[96m]─[\033[95m{info}\033[96m]\n└──╼ \033[95m"

def printBanner():
	print(banner)

def printInvitePanel():
	print(f"""
\033[96m┌──────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│\033[95m[\033[96m Admin  \033[95m]\033[96m│\033[95m{API.Utils.getAdminInvite(API.Client.getData()["botId"])}        \033[96m│
│\033[95m[\033[96mRestrain\033[95m]\033[96m│\033[95m{API.Utils.getRestrainInvite(API.Client.getData()["botId"])}\033[96m│
└──────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────┘""")

def initData():
	before = ""
	for i in range(3):
		clear()
		if i == 0:
			t = input(getPrompt("Token"))
			before += f"\033[96m> \033[95m{t}\n"
		elif i == 1:
			b = input(before + getPrompt("Bot id"))
			before += f"\033[96m> \033[95m{b}\n"
		elif i == 2:
			u = input(before + getPrompt("User id"))
	client.initData(t, u, b)