import openai
import discord

# specifying our server
GUILD = "{Creative-Tech-Apprenticeship}"

# create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())

with open("keys.txt") as f:
	# converting our text file to a list of lines
	lines = f.read().split('\n')
	# openai api key
	openai.api_key = lines[0]
	# discord token
	DISCORD_TOKEN = lines[1]
# close the file
f.close()

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break
	# print out nice statment saying our bot is online (only in command prompt)
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	# this prevents inifinte loops of bot talking to bot
	# if author of the message is the bot, don't do anything
	if message.author == client.user:
		return
	# ignore @everyone mentions
	if message.mention_everyone:
		return
	# if the message mentions the bot, then do something
	elif client.user.mentioned_in(message): 
		# this is just for kat
		response = openai.ChatCompletion.create(
			model="gpt-3.5-turbo",
			messages=[
			{"role": "system", "content": "You are a verbose art graduate student and a little insufferable."},
			{"role": "assistant": "content": "Most art is derivative"},
			{"role": "user", "content": "What makes great art?"}
			]
		)
		await message.channel.send(response.choices[0].message.content)

client.run(DISCORD_TOKEN)