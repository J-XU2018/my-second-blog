from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.seek.co.nz/jobs-in-sales").text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
# with open('html.txt', 'r+') as f:
    # f.write(soup.prettify())
div = soup.find('div', class_='_365Hwu1')
for article in div.find_all('article'):
    job_title = article.h1.text
    print(job_title)
    loc_div = article.find('div', class_='_1mzsMx5')
    location = loc_div.find('span', class_='Eadjc1o').text
    print(location)
    des_ul = article.ul
    for desc in des_ul.find_all('li'):
# print(job_title_span)
        print(desc.text)
    # print(job_title[1])
    print()
