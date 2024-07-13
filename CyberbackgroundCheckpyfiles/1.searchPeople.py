import sys
import requests
import os

def generate_search_results(strStreet, strCity, strState, apikey):
    outputfile = "temp\\searchResults.bin"
    if os.path.exists(outputfile):
        os.remove(outputfile)
        print(f"File '{outputfile}' deleted successfully.")
    strDomain = "https://www.cyberbackgroundchecks.com/address/"
    url = strDomain + strStreet + "/" + strCity + "/" + strState
    url = url.lower().strip().replace(" ", "-")

    params = {
        'url': url,
        'apikey': apikey,
        'js_render': 'true',
    }

    response = requests.get('https://api.zenrows.com/v1/', params=params)


    with open(outputfile, 'wb') as file:
        file.write(response.content)

    print("People Search Results written to " + outputfile)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script_name.py [street] [city] [state]")
    else:
        strStreet = sys.argv[1]
        strCity = sys.argv[2]
        strState = sys.argv[3]
        Apikey = sys.argv[4]
        generate_search_results(strStreet, strCity, strState, Apikey)
