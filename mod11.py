import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup
import requests


def get_frame():
    return pd.read_excel('COVID19_03242020_ByCounty.xlsx', index_col=None)

df = get_frame()

MaxCA = df[df.CasesAll == df.CasesAll.max()]
print('This is the County with the most cases.')
print(MaxCA[['COUNTYNAME', 'CasesAll', ]])
print()

Top10 = df.nlargest(10, 'CasesAll')
print('These are the 10 Counties with the highest number of cases.')
print(Top10[['COUNTYNAME', 'CasesAll', ]])
print()

df_small = Top10[['COUNTYNAME', 'CasesAll', 'C_Men', 'C_Women']]

print('This is the database I created to visualize.')
print(df_small)
print('Some of the descriptive statistics for this subset of the data.')
print(df_small.describe())
print()
#
# df_small.plot.bar()
# plt.title('The 10 Counties in Florida with the Highest Number of COVID-19 Cases')
# plt.xlabel('County')
# plt.xlabel('COVID-19 Cases')
#
# plt.tight_layout()
# plt.show()

plt.style.use("fivethirtyeight")

x_indexes = np.arange(len(df_small))
width = 0.25

plt.bar(x_indexes - width, df_small['CasesAll'], label='Total Cases', color='k', width=width)
plt.bar(x_indexes, df_small['C_Men'], label='Male Cases', color='blue', width=width)
plt.bar(x_indexes + width, df_small['C_Women'], label='Female Cases', color='#e75480', width=width)

plt.xticks(ticks=x_indexes, labels=df_small['COUNTYNAME'], fontsize=10)

plt.title('The 10 Counties in Florida with the Highest Number of COVID-19 Cases (3/24/2020)')
plt.xlabel('County')
plt.ylabel('COVID-19 Cases')
plt.legend()

# plt.tight_layout()
plt.show()

# Get some Arkansas Razorbacks Data Online
source = requests.get('https://arkansasrazorbacks.com/stats/mbb/2019-20/teamstat.htm')
# Make sure it works (aka status code = 200)
print(source.status_code)

soup = BeautifulSoup(source.content, 'html.parser')

table = soup.find('table')

# print(table)
print(table.text)
# print(type(table))

with open ('hogstats.txt', 'w') as r:
    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            r.write(cell.text.ljust(15))
        r.write('\n')

