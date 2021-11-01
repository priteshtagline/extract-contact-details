import requests
import bs4
import re


def email_list_filter(emailList):
    if len(emailList) > 1:
            for email in emailList:
                address = email.split('@')[0]
                if address.lower() == 'hr':
                    emailList.remove(email)
    return emailList

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
                    continue
                emailList.append(mail)
        
        if len(emailList) == 0:
            try:
                footer = str(soup.select('footer'))
                emailList = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z._-]+\.[a-zA-Z_-]+)', footer)
                emailList = email_list_filter(emailList)
                return emailList
            except:
                pass
        else:
            emailList = email_list_filter(emailList)
            return emailList
    except:
        pass

# def get_contact_number(soup):
#     try:
#         contact_number = soup.select_one('a[href]^=tel')
#         href = contact_number['href']
#         try:
#             x, contact_number = href.split(':')
#             return contact_number
#         except ValueError:
#             pass
#     except:
#         pass
#     try:
#         contact_number = soup.select_one('a[href]^=callto')
#         href = contact_number['href']
#         try:
#             x, contact_number = href.split(':')
#             return contact_number
#         except ValueError:
#             pass
#     except:
#         pass
#     return None

# def get_details(soup):
#     try:
#         mailtos = soup.select('a[href^=mailto]')
#         emailList = []
#         for mailto in mailtos:
#             content = mailto.parent
#             if "sales" in str(content).lower():
#                 href = mailto['href']
#                 try:
#                     x, mail = href.split(':')
#                 except ValueError:
#                     break
#                 emailList.append(mail)
#                 contact_info = get_contact_number(content)
#                 return emailList,contact_info
#             else:
#                 href = mailto['href']
#                 try:
#                     x, mail = href.split(':')
#                 except ValueError:
#                     break
#                 emailList.append(mail)
#         emailList = email_list_filter(emailList)
#         return emailList
#     except:
#         pass

urls = [
        "https://www.significantinfotech.com",
        "https://taglineinfotech.com/",
        "https://www.c-sharpcorner.com/article/how-to-validate-an-email-address-in-python/",
    ]


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
