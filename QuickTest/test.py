import requests

# Read the message from a text file
with open("message.txt", "r") as file:
    message = file.read().strip()  # Strip any leading/trailing whitespace

url = "https://cvbotapicmcgdu3.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions"
querystring = {"api-version":"2024-04-01-preview"}

# Use the variable in your payload
payload = f'{{"messages":[{{"role":"user","content":"{message}"}}]}}'

headers = {
    'content-type': "application/json",
    'api-key': "00059e9afc874e33aaadafe56faa93f0",
    'cache-control': "no-cache",
    'postman-token': "a6992ce6-39a2-e02a-9855-6e3ea6bbc5c5"
}

response = requests.post(url, data=payload, headers=headers, params=querystring)

print(response.text)
