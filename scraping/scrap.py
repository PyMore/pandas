import pandas as pd
import requests
import pymongo
from bs4 import BeautifulSoup
from tabulate import tabulate
# package mongodb
from pymongo import MongoClient


class MongoDB():
    def __int__(self):
        pass

    def showConections(self):
        pass


def get_info(Contrib):
    res = requests.get("https://es.wikipedia.org/wiki/"+Contrib)
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    print(tabulate(df[0], headers='keys', tablefmt='psql'))


# Demo connect
client = MongoClient('localhost',27017)
db = client.database_names()
print(db)

print(client)


