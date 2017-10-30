import pandas as pd
import requests
import pymongo
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
        soup = BeautifulSoup(res.content, 'lxml')
        table = soup.find_all('table')[0]
        df = pd.read_html(str(table))
        print(tabulate(df[0], headers='keys', tablefmt='psql'))


sp = Scrap()
sp.showDB()
sp.get_info("Alemania")
