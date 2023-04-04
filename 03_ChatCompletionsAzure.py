import openai

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

with open("keys.txt") as f:
	# converting our text file to a list of lines
	lines = f.read().split('\n')
	# openai api key
	openai.api_key = lines[0]
	openai.api_base = lines[2]
# close the file
f.close()

response = openai.ChatCompletion.create(
	engine="GPT-4",
	messages=[
	{"role": "system", "content": "You are a small child, most things amuse you. Make sure all responses are less than 2000 characters"},
	{"role": "user", "content": "What's the best thing to do when your code is broken?"}
	]
)
print(response.choices[0].message.content)