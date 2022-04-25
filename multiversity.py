import requests
import os
import openai

# Perchance Custom API
r = requests.get('https://alternate-histories.glitch.me/api?generator=3ldrg8lxwn&list=output')

rprompt = r.text

openai.api_key = "YOUR API KEY HERE"

length = 800

response = openai.Completion.create(
    engine = "text-davinci-002",
    prompt = rprompt,
    temperature = 1,
    max_tokens = length,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
)

print(rprompt)
print(response.choices[0].text)