import discord, requests, os, asyncio, colorama, time, asyncio, threading, sys
from pypresence import Presence
from colorama import Fore
from discord.ext import commands

os.system('cls & mode 50,20 & title Cope - Config')
token = input(f"[{Fore.RED}Cope{Fore.RESET}]~ Token{Fore.RED}: {Fore.RESET}")
rpresence = input(f'[{Fore.RED}Cope{Fore.RESET}]~ Rich Presence (Y \ N){Fore.RED}: {Fore.RESET}')

def RichPresence():
    if rpresence.upper() == "y" or rpresence.lower() == "y":
        try:
            RPC = Presence("829084497655234571")
            RPC.connect()
            RPC.update(large_image="8",details="Cry with me?",buttons=[{"label":"Github","url":"https://github.com/7BZ"}],start=time.time())
        except:
            pass
rpresence = RichPresence()

client = commands.Bot(command_prefix=">",self_bot=True,intents=discord.Intents.all())
client.remove_command('help')

class Cope:
	def __init__(self):
		pass

	async def ChannelCopy(self):
			urguild = input(f"[{Fore.RED}Cope{Fore.RESET}]~ Your Guild ID{Fore.RED}: {Fore.RESET}")
			guild = input(f"[{Fore.RED}Cope{Fore.RESET}]~ Guild ID{Fore.RED}: {Fore.RESET}")
			guildOBJ = client.get_guild(int(guild))
			guildOBJ2 = client.get_guild(int(urguild))
			for cate in guildOBJ.categories:
				x = await guildOBJ2.create_category(cate.name)
				for chann in cate.channels:
					if isinstance(chann, discord.VoiceChannel):
						await x.create_voice_channel(chann.name)
					if isinstance(chann, discord.TextChannel):
						await x.create_text_channel(chann.name)


	async def DeleteChannels(self):
			urguild = input(f"[{Fore.RED}Cope{Fore.RESET}]~ Your Guild ID{Fore.RED}: {Fore.RESET}")
			guildOBJ2 = client.get_guild(int(urguild))
			for c in guildOBJ2.channels:
				await c.delete()


	async def RolesCopy(self):
		urguild = input(f"[{Fore.RED}Cope{Fore.RESET}]~ Your Guild ID{Fore.RED}: {Fore.RESET}")
		guild = input(f"[{Fore.RED}Cope{Fore.RESET}]~ Guild ID{Fore.RED}: {Fore.RESET}")
		guildOBJ = client.get_guild(int(guild))
		guildOBJ2 = client.get_guild(int(urguild))
		roles = guildOBJ.roles
		for x in range(len(roles)):
			if roles[-x].name == guildOBJ2.default_role.name:
				await guildOBJ2.default_role.edit(permissions=roles[x].permissions)
			else:
				await guildOBJ2.create_role(name=roles[-x].name,permissions=roles[-x].permissions,colour=roles[-x].colour)


	async def DeleteRoles(self):
		urguild = input(f"[{Fore.RED}Cope{Fore.RESET}]~ Your Guild ID{Fore.RED}: {Fore.RESET}")
		guildOBJ2 = client.get_guild(int(urguild))
		for a in guildOBJ2.roles:
			if a.name == guildOBJ2.default_role.name:
				pass
			elif a.managed == False:
				await a.delete()
			else:
				pass

	async def GuildPic(self):
		guild = input(f"[{Fore.RED}Cope{Fore.RESET}]~ Guild ID{Fore.RED}: {Fore.RESET}")
		guildOBJ = client.get_guild(int(guild))
		r = requests.get(guildOBJ.icon_url)
		with open(f'{guildOBJ.name}.gif','wb') as f:
			f.write(r.content)
			f.close()


	def Message(self):
		print(f'''
[{Fore.RED}HELP{Fore.RESET}] - Help
[{Fore.RED}1{Fore.RESET}] - Copy Channels
[{Fore.RED}2{Fore.RESET}] - Copy Roles
[{Fore.RED}3{Fore.RESET}] - Delete Channels
[{Fore.RED}4{Fore.RESET}] - Delete Roles
[{Fore.RED}5{Fore.RESET}] - Copy Guild Icon
[{Fore.RED}C{Fore.RESET}] - Credits''')

	def Message2(self):
		print(f'''
[{Fore.RED}Github{Fore.RESET}] - 7BZ''')

	async def Menu(self):
		os.system(f"""cls & mode 50,20 & title Cope - User: {client.user}""")
		print(f'''
{Fore.LIGHTBLACK_EX} ▄█▄    ████▄ █ ▄▄  ▄███▄
{Fore.LIGHTBLACK_EX} █▀ ▀▄  █   █ █   █ █▀   ▀
{Fore.LIGHTBLACK_EX} █   ▀  █   █ █▀▀▀  ██▄▄    {Fore.RESET} Type {Fore.RED}HELP {Fore.RESET}For Help.
{Fore.LIGHTBLACK_EX} █▄  ▄▀ ▀████ █     █▄   ▄▀ {Fore.RESET} Made by {Fore.RED}sordo{Fore.RESET}
{Fore.LIGHTBLACK_EX} ▀███▀         █    ▀███▀
{Fore.LIGHTBLACK_EX}                ▀
{Fore.RESET}''')
		outputz = input(f"[{Fore.RED}Cope{Fore.RESET}]~ {Fore.RED}: {Fore.RESET}")
		if outputz.lower() == "help" or outputz.upper() == "help":
			self.Message()
			time.sleep(2)
			await self.Menu()
		elif outputz == "1":
			await self.ChannelCopy()
			time.sleep(2)
			await self.Menu()
		elif outputz == "2":
			await self.RolesCopy()
			time.sleep(2)
			await self.Menu()
		elif outputz == "3":
			await self.DeleteChannels()
			time.sleep(2)
			await self.Menu()
		elif outputz == "4":
			await self.DeleteRoles()
			time.sleep(2)
			await self.Menu()
		elif outputz == "5":
			await self.GuildPic()
			time.sleep(2)
			await self.Menu()
		elif outputz.lower() == "c" or outputz.upper() == "c":
			self.Message2()
			time.sleep(2)
			await self.Menu()
		else:
			time.sleep(2)
			await self.Menu()

@client.event
async def on_error(error):
	with open('errors.txt','a') as f:
		f.write(f"Error: Improper Guild ID has been passed.\n")
		f.close()
	time.sleep(2)
	await Cope().Menu()

@client.event
async def on_ready():
	await Cope().Menu()

try:
	client.run(token,bot=False)
except Exception as e:
	with open('errors.txt','a') as f:
		f.write(f"Error: {e}\n")
		f.close()
