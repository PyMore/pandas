import math
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
# package mongodb
from pymongo import MongoClient


class Scrap:

    def __init__(self):
        """Initializes the data."""
        self.client = MongoClient('localhost', 27017)
        print("(Initializing {})".format(self.client))

    def showDB(self):
        print(self.client.database_names())

    def saveConllections(self):
        print('Save collections')

    def showCollections(self):
        print('Show Collections')

    def get_info(self, contrib):
        res = requests.get("https://es.wikipedia.org/wiki/"+contrib)
        print(res)
        soup = BeautifulSoup(res.content, 'lxml')
        table = soup.find_all('table')[0]
        dfHtml = pd.read_html(str(table))

        # Table
        print(tabulate(dfHtml[0], headers='keys', tablefmt='psql'))


        for  element in dfHtml[0][0]:
            if type(element) is float:
                if math.isnan(element) is not True:
                    print(element)
            else:
                print(element)

        print('\n'*1)





sp = Scrap()
sp.showDB()
sp.get_info("Alemania")
