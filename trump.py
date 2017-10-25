import numpy as np
import pandas as pd

#Read csv

expected_files = [
    'src/tweets.csv',
    'src/news.csv',
    'src/issue-1.csv',
    'src/issue-2.csv',
    'src/issue-3.csv',
    'src/issue-4.csv',
    'src/issue-5.csv',
    'src/TRUMPWORLD-pres.csv',
    'src/TRUMPWORLD-us.csv',
]

tweets = pd.read_csv(expected_files[0])
news = pd.read_csv(expected_files[1])

#issue


issue1 = pd.read_csv(expected_files[2])
issue2 = pd.read_csv(expected_files[3])
issue3 = pd.read_csv(expected_files[4])
issue4 = pd.read_csv(expected_files[5])
issue5 = pd.read_csv(expected_files[6])
pres = pd.read_csv(expected_files[7])
us = pd.read_csv(expected_files[8])

print(us)
