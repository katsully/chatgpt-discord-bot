import discord

with open("keys.txt") as f:
	# converting our text file to a list of lines
	lines = f.read().split('\n')
	# discord token
	DISCORD_TOKEN = lines[0]
# close the file
f.close()

# specifying our server
GUILD = "{Creative-Tech-Apprenticeship}"

# create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break
	# print out nice statment saying our bot is online (only in command prompt)
	print(f'{client.user} has connected to Discord!')

client.run(DISCORD_TOKEN)