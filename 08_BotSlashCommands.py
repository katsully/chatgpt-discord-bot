import openai
import discord

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

# create an object that will control our discord bot
bot = discord.Bot(intents=discord.Intents.default())

with open("keys.txt") as f:
	# converting our text file to a list of lines
	lines = f.read().split('\n')
	# openai api key
	openai.api_key = lines[0]
	# discord token
	DISCORD_TOKEN = lines[1]
	openai.api_base = lines[2]
# close the file
f.close()

@bot.event
async def on_ready():
	# await bot.sync()
	# print out nice statment saying our bot is online (only in command prompt)
	print('Our bot has connected to Discord!')

@bot.command(description="Say hello")  
async def first_slach(ctx):  
    await ctx.respond("Hello!")

bot.run(DISCORD_TOKEN)