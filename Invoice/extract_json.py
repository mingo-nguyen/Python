import json

# Your response as a JSON string
with open(response_file, "r", encoding="utf-8") as file:
    response = file.read().strip()


# Parse the JSON response
data = json.loads(response)

# Extract the message content
message_content = data['choices'][0]['message']['content']

print(message_content)
