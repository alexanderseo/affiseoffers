import requests
import pandas as pd
import json


class InfoMethodsOffers:
    base_endpoints = 'http://api.cpanomer1.affise.com/3.0/'

    def __init__(self, headers):
        self.headers = headers

    def offersListToJson(self):
        try:
            affise_response = requests.get(InfoMethodsOffers.base_endpoints + 'offers', headers=self.headers)
            affise_response.raise_for_status()
            json_response = affise_response.json()
            with open('alloffers.json', 'w', encoding='utf-8') as file:
                json.dump(json_response, file, indent=2, ensure_ascii=False)
            print('Документ с доступными Офферами создан: alloffers.json')
        except requests.exceptions.HTTPError as errorhttp:
            print("Http Error:", errorhttp)
        except requests.exceptions.ConnectionError as errorconnection:
            print("Error Connecting:", errorconnection)
        except requests.exceptions.Timeout as errortimeout:
            print("Timeout Error:", errortimeout)
        except requests.exceptions.RequestException as error:
            print("Oops: Something Else", error)


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
        try:
            affise_response = requests.get(InfoMethodsOffers.base_endpoints + 'offers?countries=' + categories, headers=self.headers)
            affise_response.raise_for_status()
            json_response = affise_response.json()
            with open('offersbycategories.json', 'w', encoding='utf-8') as file:
                json.dump(json_response, file, indent=2, ensure_ascii=False)
            print('Документ c офферами по категории создан: offersbycategories.json')
        except requests.exceptions.HTTPError as errorhttp:
            print("Http Error:", errorhttp)
        except requests.exceptions.ConnectionError as errorconnection:
            print("Error Connecting:", errorconnection)
        except requests.exceptions.Timeout as errortimeout:
            print("Timeout Error:", errortimeout)
        except requests.exceptions.RequestException as error:
            print("Oops: Something Else", error)

    def offerCategoriesToJson(self):
        try:
            affise_response = requests.get(InfoMethodsOffers.base_endpoints + 'offer/categories', headers=self.headers)
            affise_response.raise_for_status()
            json_response = affise_response.json()
            with open('offercategories.json', 'w', encoding='utf-8') as file:
                json.dump(json_response, file, indent=2, ensure_ascii=False)
            print('Документ c доступными категориями офферов создан: offersbycategories.json')
        except requests.exceptions.HTTPError as errorhttp:
            print("Http Error:", errorhttp)
        except requests.exceptions.ConnectionError as errorconnection:
            print("Error Connecting:", errorconnection)
        except requests.exceptions.Timeout as errortimeout:
            print("Timeout Error:", errortimeout)
        except requests.exceptions.RequestException as error:
            print("Oops: Something Else", error)

    def tableViewForOfferCategories(self):
        with open("offercategories.json", encoding='utf-8') as file_offers:
            read_file_offers = file_offers.read()
            z = json.loads(read_file_offers)
            offers = pd.json_normalize(z, 'categories')
            print(offers)

    def offerById(self, ID):
        try:
            affise_response = requests.get(InfoMethodsOffers.base_endpoints + 'offer/' + ID, headers=self.headers)
            affise_response.raise_for_status()
            json_response = affise_response.json()
            with open('offerID.json', 'w', encoding='utf-8') as file:
                json.dump(json_response, file, indent=2, ensure_ascii=False)
            print('Документ с оффером %s: offerID.json' % ID)
        except requests.exceptions.HTTPError as errorhttp:
            print("Http Error:", errorhttp)
        except requests.exceptions.ConnectionError as errorconnection:
            print("Error Connecting:", errorconnection)
        except requests.exceptions.Timeout as errortimeout:
            print("Timeout Error:", errortimeout)
        except requests.exceptions.RequestException as error:
            print("Oops: Something Else", error)

    def resultInfoOfferID(self):
        with open("offerID.json", encoding='utf-8') as fileoffers:
            readfileoffers = fileoffers.read()
            z = json.loads(readfileoffers)
            offers = pd.json_normalize(z)
        offer_ID = pd.Series(offers['offer.id'])
        offer_Title = pd.Series(offers['offer.title'])
        offer_Countries = pd.Series(offers['offer.countries'])
        return 'Оффер ID: {0} - {1}, страны в Оффере: {2}'.format(offer_ID.item(), offer_Title.item(), offer_Countries.item())




if __name__ == "__main__":
    headers = {'API-Key': ''}
    x = InfoMethodsOffers(headers)
    print(x.resultInfoOfferID())