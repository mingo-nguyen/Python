import sys
import os
from bs4 import BeautifulSoup


def find_relative_url(strFirstName, strLastName):
    outputfile = "temp\\relativeURL.txt"
    if os.path.exists(outputfile):
        os.remove(outputfile)
        print(f"File '{outputfile}' deleted successfully.")

    with open('temp\\searchResults.bin', 'rb') as file:
        binary_content = file.read()

    # Parse the binary content with BeautifulSoup
    soup = BeautifulSoup(binary_content, "html.parser")
    name_nodes = soup.find_all(class_="name-given")
    name_node = None
    isFound = False
    strRelativeURL = None
    for item in name_nodes:
        print(item.text.lower().strip())
        if strFirstName.lower().strip() in item.text.lower().strip() and strLastName.lower().strip() in item.text.lower().strip():
            name_node = item
            if name_node:
                details_link = name_node.find_parent("div", class_="card").find("a", title=lambda
                    value: value and "View full address history" in value)
                if details_link:
                    print(details_link.get("href"))
                    strRelativeURL = details_link.get("href")
                    isFound = True
                    break
                else:
                    print(f"Details link not found for {item.text.strip()}")
            else:
                print("Node with specified name not found.")

    with open(outputfile, "w") as file:
        if isFound == True:
            file.write(strRelativeURL)
        else:
            file.write("No URL")
    print("Relative URL Details written to", outputfile)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py [first_name] [last_name]")
    else:
        strFirstName = sys.argv[1]
        strLastName = sys.argv[2]
        find_relative_url(strFirstName, strLastName)
