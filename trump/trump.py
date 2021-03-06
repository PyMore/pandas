import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from statistics import mean

##############
# Read csv
#############

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
dtnews = pd.DataFrame(news)

##################
# DataFrame issue
##################

dtIssue1 = pd.DataFrame(issue1)
dtIssue2 = pd.DataFrame(issue2)
dtIssue3 = pd.DataFrame(issue3)
dtIssue4 = pd.DataFrame(issue4)
dtIssue5 = pd.DataFrame(issue5)


totalIssue1 = (dtIssue1[['Disapprove']].values.sum())-\
              (dtIssue1[['Approve']].values.sum())

totalIssue2 = (dtIssue2[['Disapprove']].values.sum())-\
              (dtIssue2[['Approve']].values.sum())

totalIssue3 = (dtIssue3[['Disapprove']].values.sum())-\
              (dtIssue3[['Approve']].values.sum())

totalIssue4 = (dtIssue4[['Disapprove']].values.sum())-\
              (dtIssue4[['Approve']].values.sum())

totalIssue5 = (dtIssue5[['Disapprove']].values.sum())-\
              (dtIssue5[['Approve']].values.sum())

####################
# average Disapprove
###################


#####################
# matplotlib issues
#####################

names = [
    'issue1',
    'issue2',
    'issue3',
    'issue4',
    'issue5'
]
values = [
    totalIssue1,
    totalIssue2,
    totalIssue3,
    totalIssue4,
    totalIssue5
]

plt.figure(1, figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.grid(True)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Issues')
plt.show()


