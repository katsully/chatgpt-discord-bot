import openai

with open("keys.txt") as f:
	# converting our text file to a list of lines
	lines = f.read().split('\n')
	# openai api key
	openai.api_key = lines[0]
	# discord token
	DISCORD_TOKEN = lines[1]
# close the file
f.close()

response = openai.Image.create(
  prompt="a beautiful London spring day, vintage vibes, muted colors",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)