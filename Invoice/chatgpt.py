import requests
import json
import argparse
import os

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Send a message to an API and save the response.')
    
    # Add the arguments
    parser.add_argument('--message', type=str, required=True, help='The message to be sent')
    parser.add_argument('--filename', type=str, required=True, help='The filename to save the response')
    parser.add_argument('--api-key', type=str, required=True, help='Your API key')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Access the arguments
    message = args.message
    filename = args.filename
    api_key = args.api_key

    # URL and query parameters
    url = "https://cvbotapicmcgdu3.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions"
    querystring = {"api-version":"2024-04-01-preview"}

    # Construct the payload
    payload_dict = {
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }
    
    # Convert the dictionary to a JSON string
    payload = json.dumps(payload_dict)

    # Headers for the request
    headers = {
        'content-type': "application/json",
        'api-key': api_key,
        'cache-control': "no-cache"
    }

    # Send the POST request
    response = requests.post(url, data=payload, headers=headers, params=querystring)
    raw_response_file = f"{os.path.splitext(filename)[0]}_rawresponse.txt"
    output_txt_path = f"{os.path.splitext(filename)[0]}_dataJson.txt"
    # Print the response text
    print(response.text)
    with open(raw_response_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(response.text)
        
        
    # Process the response
    data = json.loads(response.text)
    message_content = data['choices'][0]['message']['content']


    
    # Save the processed message content to another file
    with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(message_content)

if __name__ == '__main__':
    main()
