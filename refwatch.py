import requests
from bs4 import BeautifulSoup
from datetime import datetime
from db import insert

URL = "https://www.referendum2021.sk/"
SELECTOR = ".totalcount strong"

def main():
    response = requests.get(URL)

    bs = BeautifulSoup(response.content, features="lxml")

    elements = bs.select(SELECTOR)

    number = int(elements[0].text.replace(" ", ""))

    timestamp = datetime.now().timestamp()

    insert(number, timestamp)

if __name__ == "__main__":
    main()



