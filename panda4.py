#group by and aggregating
import pandas as pd
df = pd.read_csv(r'C:\Users\HP\Downloads\Flavors.csv')

#grouping by base flavor coz its not unique and duplicate values on different rows
#print(df.groupby('Base Flavor')) # once you do this it will create its own obj.
group_by_frame = df.groupby('Base Flavor')
#print(group_by_frame.mean())# the average- with this code you will get an error
## TypeError: agg function failed [how->mean,dtype->object]
# to fix the error you need to limit the mean output to only (numeric_only=True)
#mean_values = group_by_frame.mean(numeric_only=True)
# print(mean_values)
#USING ONE LINER
#df.groupby('Base Flavor').mean(numeric_only = True)

# An aggregate is a function where the values of multiple rows are grouped together to form a single summary value.
#count of the rows that were aggregrated
# count_group = df.groupby("Base Flavor").count()
# print(count_group)

#min
# count_group = df.groupby("Base Flavor").min()# it is using string to alphabetize the data
# print(count_group)

#max
# count_group = df.groupby("Base Flavor").max()
# print(count_group)

#sum
# count_group = df.groupby("Base Flavor").sum()


# this is our aggregrate function
#print(df.groupby("Base Flavor").agg({'Flavor Rating':['mean','max','count','sum'],'Texture Rating':['mean','max','count','sum']}))
#output
#          Flavor Rating
#                      mean   max count   sum
# Base Flavor
# Chocolate             8.4   8.8     3  25.2
# Vanilla               5.7  10.0     6  34.2

#grouping multiple columns
print(df.groupby(['Base Flavor','Liked']).mean(numeric_only=True))
print(df.groupby(['Base Flavor','Liked']).agg({'Flavor Rating':['mean','max','count','sum'],'Texture Rating':['mean','max','count','sum']}))

# shortcut
print(df.groupby('Base Flavor').describe())
# output
#           Flavor Rating                      ... Total Rating
#                     count mean       std  min  ...          25%   50%     75%   max
# Base Flavor                                    ...
# Chocolate             3.0  8.4  0.346410  8.2  ...       15.250  15.3  15.950  16.6
# Vanilla               6.0  5.7  2.710719  2.3  ...        9.025  11.1  13.175  18.0

