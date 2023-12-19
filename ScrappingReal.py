# from bs4 import BeautifulSoup
# import requests
#
# url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
# page = requests.get(url)
# print(page)
#
# soup = BeautifulSoup(page.text,'html')
#
# # now were gonna want the headers than the data , be aware there are two tables
# print(soup.find_all('table')[1])
#
#
# # the exact table we are looking for is
# # print(soup.find('table',class_= 'wikitable sortable'))
# table = soup.find_all('table')[1] # the [1] is using indexing to get the first table
# print(table)
#
# #now we want to get the title(of columns) of the tables- they are the th -tags
# world_titles = table.find_all('th')
# world_table_titles = [title.text.strip() for title in world_titles]# to put .strip() to clean- remove the backslashes
#
# print(world_table_titles)
#
# #now we are storind the headers since tables so pandas
# import pandas as pd
# df = pd.DataFrame(columns= world_table_titles)
# print(df)
#
# # now we need to pull data from with in the columns
# # tr = row , d = data itself
# column_data = table.find_all('tr')
#
# for row in column_data[1:]:
#     row_data = row.find_all('td')
#     individual_row_data = [data.text.strip() for data in row_data]
#     print(individual_row_data)
#
#     length = len(df)
#     df.loc[length] = individual_row_data
#
# # incase you need to export this table into a csv
# #df.to_csv(r'C:\Users\HP\Desktop\Companies.csv') # this will print out including the index
# # which would make it ugly, to remove the index  to below
# df.to_csv(r'C:\Users\HP\Desktop\testfiles\Companies.csv',index = False)

from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
print(page)
soup = BeautifulSoup(page.text, 'html')
table = soup.find_all('table')[1]
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

import pandas as pd
df = pd.DataFrame(columns= world_table_titles)
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df) # how many columns in our dataframe is our length
    df.loc[length] = individual_row_data































