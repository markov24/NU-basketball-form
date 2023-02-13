import sys
import requests
import time
from bs4 import BeautifulSoup

if len(sys.argv)>2:
    print(f"You have provided {len(sys.argv)-1} inputs")
    print("Only provide 1 input string: Name of NU's opposing basketball team")
    sys.exit()

url = "https://nusports.com/sports/2023/1/13/northwestern-wildside-student-ticket-request-information"

def is_string_in_webpage(string_to_search):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return string_to_search in soup.get_text()
    else:
        return False

search_string = sys.argv[1]
while True:
    time.sleep(1)
    result = is_string_in_webpage(search_string)
    if result:
        print("FORM IS OUT")
        sys.exit()
