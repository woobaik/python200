import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser')
table_body = soup.find('tbody')
table_row = table_body.find_all('tr')

countries_data = []

for tr in table_row:
    tds = tr.find_all('td')
    if tds[1].string != "No universal currency":

        countries_data.append(tds)


def countries_print():
    for idx, country in enumerate(countries_data):
        print(f"# {idx} {country[0].string}")


def get_user_input():
    not_valid = True
    while not_valid:
        try:
            user_input = int(
                input("Hello! Please choose select a country by number:"))
            if not 0 <= user_input <= 267:
                print("Choose a number from the list.")
            not_valid = False

        except ValueError:
            print("That wasn't a number.")

    return user_input


def fetch_country_info_from_input(input):
    fetched_data = countries_data[input]
    print(f"You chose {fetched_data[0].string}")
    print(f"The currency code is {fetched_data[2].string}")


countries_print()
fetch_country_info_from_input(get_user_input())
