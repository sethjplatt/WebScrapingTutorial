import json
import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/List_of_assassinations"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')


countries = soup.find_all('h3')

dict = {}

for country in countries:
    countryName = country.span.text.strip()
    countryAssassinations = {}

    table = country.find_next('tbody')

    for row in table:
        date = row.find_next('td').text.strip()
        victim = row.find_next('td').find_next('td').text.strip()

        countryAssassinations[date] = victim

    dict[countryName] = countryAssassinations

with open('data.json', 'w') as dataFile:
    json.dump(dict, dataFile)



# {
#     countryName: {
#       date: victim,
#       date: victim
#     },
#     countryName: {
#       date: victim,
#       date: victim
#     }
# }


















# from bs4 import BeautifulSoup
# import requests
# import json

# url = 'https://en.wikipedia.org/wiki/List_of_assassinations'

# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html.parser')

# countries = soup.find_all('h3')

# dict = {}

# for country in countries:
#     countryName = country.span.text
#     countryAssassinations = {}

#     table = country.find_next('tbody')

#     for row in table:
#         date = row.find_next('td').text.strip()
#         victim = row.find_next('td').find_next('td').text.strip()
#         print(victim)
#         countryAssassinations[date] = victim

#     dict[countryName] = countryAssassinations


# with open('assassinations.json', 'w') as file:
#     json.dump(dict, file)

# {
#     countryName: {
#       date: victim,
#       date: victim
#     },
#     countryName: {
#       date: victim,
#       date: victim
#     }
# }



