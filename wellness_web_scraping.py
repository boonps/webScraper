# import csv
#
# import requests
# from bs4 import BeautifulSoup as bs
#
# URL = 'https://retty.co.th/area/PRO10/page-{}'
# save_to = []
# for page in range(1, 4):
#     req = requests.get(URL.format(page))
#     soup = bs(req.text, 'html.parser')
#
#     titles = soup.find_all('span', 'restaurant-card__name')
#     # print(titles)
#
#     for names in titles:
#         add = save_to.append(names.get_text())
#         # print(names.get_text())
#
# # print(save_to)
# with open("name_wellness.csv", 'w') as f1:
#     write = csv.writer(f1, delimiter=',')
#     write.writerows([x.split(',') for x in save_to])

import xlsxwriter
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://retty.co.th/area/PRO10/page-{}'
save_to = []
for page in range(1, 4):
    req = requests.get(URL.format(page))
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('span', 'restaurant-card__name')
    # print(titles)

    for names in titles:
        add = save_to.append(names.get_text())
        # print(names.get_text())

# print(save_to)
workbook = xlsxwriter.Workbook('name_wellness.xlsx')
worksheet = workbook.add_worksheet()
row = 0
column = 0
for item in save_to:
    # write operation perform
    worksheet.write(row, column, item)

    # incrementing the value of row by one
    # with each iterations.
    row += 1

# workbook.close()


# #################
# read / save ###########
# ##############
