import requests
from bs4 import BeautifulSoup

url = 'https://retty.co.th/area/PRO10/page-6'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# new = soup.find('div')
new = soup.find_all('span', 'restaurant-card__name')
# span_tag = new.find_all('a')
print(new)
for names in new:
    print(names.get_text())

    # #################
    # read only ###########
    # ##############
