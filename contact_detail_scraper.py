import requests
import bs4
import re


def get_email(soup):
    try:
        mailtos = soup.select('a[href^=mailto]')
        emailList = []
        for mailto in mailtos:
            content = str(mailto.parent)
            if "sales" in content.lower():
                emailList.clear()
                href = mailto['href']
                try:
                    x, mail = href.split(':')
                except ValueError:
                    break
                emailList.append(mail)
                return emailList
            else:
                href = mailto['href']
                try:
                    x, mail = href.split(':')
                except ValueError:
                    break
                emailList.append(mail)
        return emailList
    except:
        pass


urls = ["https://www.significantinfotech.com/about-us/",
        "https://taglineinfotech.com/",]


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

detail_list = []

for url in urls:
    try:
        response = requests.get(url, headers=headers)
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
