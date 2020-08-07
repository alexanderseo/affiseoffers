import requests
import pandas as pd
import json


class GetAllOffers:
    base_endpoints = 'http://api.cpanomer1.affise.com/3.0/'

    def __init__(self, headers):
        self.headers = headers

    def offersListToJson(self):
        affise_response = requests.get(GetAllOffers.base_endpoints + 'offers', headers=self.headers)
        json_response = affise_response.json()
        with open('alloffers.json', 'w', encoding='utf-8') as file:
            json.dump(json_response, file, indent=2, ensure_ascii=False)

    def readOffersFile(self):
        with open("alloffers.json", encoding='utf-8') as fileoffers:
            read_file_offers = fileoffers.read()
            loads_file_offers = json.loads(read_file_offers)
            offers = pd.json_normalize(loads_file_offers)

        data_from_pandas_series = pd.Series(offers.offers)
        for i in data_from_pandas_series:
            # Можно вывести все в табличном виде, дописать метод и импортнуть в таблицу с нужными столбцами
            table = pd.DataFrame(i, columns=['id', 'title' 'countries'])
            print(table)

    def offersListByCategoriesToJson(self, categories):
        affise_response = requests.get(GetAllOffers.base_endpoints + 'offers' + '?' 'categories' + '=' + categories, headers=self.headers)
        json_response = affise_response.json()
        with open('offersbycategories.json', 'w', encoding='utf-8') as file:
            json.dump(json_response, file, indent=2, ensure_ascii=False)

    def offerCategoriesToJson(self):
        affise_response = requests.get(GetAllOffers.base_endpoints + 'offer/categories', headers=self.headers)
        json_response = affise_response.json()
        with open('offercategories.json', 'w', encoding='utf-8') as file:
            json.dump(json_response, file, indent=2, ensure_ascii=False)

    def tableViewForOfferCategories(self):
        with open("offercategories.json", encoding='utf-8') as file_offers:
            read_file_offers = file_offers.read()
            z = json.loads(read_file_offers)
            offers = pd.json_normalize(z, 'categories')
            print(offers)


if __name__ == "__main__":
    headers = {'API-Key': 'e60a98867d363b0d43b9e7c58ec498ed'}
    x = GetAllOffers(headers)
    x.tableViewForOfferCategories()