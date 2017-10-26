import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

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

#############
# issue
#############

issue1 = pd.read_csv(expected_files[2])
issue2 = pd.read_csv(expected_files[3])
issue3 = pd.read_csv(expected_files[4])
issue4 = pd.read_csv(expected_files[5])
issue5 = pd.read_csv(expected_files[6])

pres = pd.read_csv(expected_files[7])
us = pd.read_csv(expected_files[8])

##############
# DataFrame
##############

dtTweets = pd.DataFrame(tweets)
#print("\n"*4)
dtnews = pd.DataFrame(news)
#print("\n"*4)

##################
# DataFrame issue
##################

dtIssue1 = pd.DataFrame(issue1)
dtIssue2 = pd.DataFrame(issue2)
dtIssue3 = pd.DataFrame(issue3)
dtIssue4 = pd.DataFrame(issue4)
dtIssue5 = pd.DataFrame(issue5)

print(issue3)

print(dtIssue1[['net_approval']].values.sum())

plt.plot([dtIssue1[['net_approval']]\
         .values.sum(),
          dtIssue2[['net_approval']]\
         .values.sum(),
          dtIssue3[['net_approval']]\
         .values.sum(),
          dtIssue2[['net_approval']] \
         .values.sum()
])
plt.ylabel('net_approval')
plt.show()