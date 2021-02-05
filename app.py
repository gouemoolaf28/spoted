import requests
from main import add_brand
from datetime import date


def scraper(pageNumber=0):

    try:

        url = f"https://api.spoted.co/brands?limit=32&offset={pageNumber}&search=&productCategories=&collections=&prices=&minimumAmounts=&vendors"

        payload={}
        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        datas = response.json()

        for data in datas:
            id = data['id']
            name = data['name']
            country = data['vendor']['country']

            brands = {
                'id': id,
                'name': name,
                'country': country,
                'date': date.today()
            }

            print(brands)

            
            add_brand(brands['id'], brands['name'],brands['country'], brands['date'])
        pageNumber += 32
        scraper(pageNumber=pageNumber)

    except RecursionError:
        return

scraper()