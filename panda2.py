# https://www.youtube.com/watch?v=kB7FV-ijdqE&list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF&index=58&t=11s
import pandas as pd
df = pd.read_csv(r'C:\Users\HP\Downloads\world_population.csv')
#print(df.info())
# print(df.head())

#print(df[df['Rank']<10]) # to print out the ranks that are less than 10 stated in df.info()

#now we are checking if a particular data exist like IS IN  - sql function
# specific_countries = ['Bangladesh','Brazil']
# print(df[df['Country'].isin(specific_countries)])
# https://www.youtube.com/watch?v=kB7FV-ijdqE&list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF&index=58&t=11s

# using contains similar to isin
#print(df[df['Country'].str.contains('United')])

# you can actually set what column to use as index(for .iloc) by
df2 = df.set_index('Country')
# another option for .loc(very specific) - filter more wide
#df2.filter(items = ['Continent','CCA3'])
# now you can specify  where it will look from the rows = axis 0 or column = axis 1
#print(df2.filter(items = [ 'Continent','CCA3'],axis =1))
# another option to  the contains
#print(df2.filter(like = 'United',axis = 0))

# print(df2.loc['United States'])


# ordering and sorting the values in the tables.
print(df[df['Rank'] < 10].sort_values(by='Rank',ascending  =False))

#multiple columns - take note that you can control the ascending or descending per column
print(df[df['Rank'] < 10].sort_values(by=['Rank','Country'],ascending  =[False,True]))
