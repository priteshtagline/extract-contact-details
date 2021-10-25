import requests
import bs4
import re

def get_email(soup):
    try:
        mailtos = soup.select('a[href^=mailto]')
        for i in mailtos:
            href=i['href']
            try:
                x, mail = href.split(':')
            except ValueError:
                break
            return mail
    except:
        pass

urls = ["https://www.significantinfotech.com/about-us/",
        "https://taglineinfotech.com/",]

detail_list = []
for url in urls:
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
    except:
        continue

    email = get_email(soup)
    detail = {
        'link': (response.url),
        'email': email,
    }
    detail_list.append(detail)

print(detail_list)