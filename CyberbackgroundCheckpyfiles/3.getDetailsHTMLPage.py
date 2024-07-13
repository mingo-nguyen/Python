import sys
import os
import requests
def fetch_details(apiKey):
    outputfile = 'temp\\details.bin'
    if os.path.exists(outputfile):
        os.remove(outputfile)
        print(f"File '{outputfile}' deleted successfully.")

    with open('temp\\relativeURL.txt', 'r') as f:
        # Read the entire contents of the file
        strRelativeURL = f.read()
        print(strRelativeURL)

    if strRelativeURL != "No URL":
        url = "https://www.cyberbackgroundchecks.com" + strRelativeURL
        params = {
            'url': url,
            'apikey': apiKey,
            'js_render': 'true',
        }
        response = requests.get('https://api.zenrows.com/v1/', params=params)
        with open(outputfile, 'wb') as file:
            file.write(response.content)
    else:
        with open(outputfile, 'wb') as file:
            file.write("No URL".encode('utf-8'))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py [apiKey]")
    else:
        apiKey = sys.argv[1]
        fetch_details(apiKey)
