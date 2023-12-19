#indexing
import pandas as pd
df = pd.read_csv(r'C:\Users\HP\Downloads\world_population.csv',index_col='Country')
#setting the index the other way
# d2= df.set_index('Country',inplace= True) # inplace so it will stick
#print(df)

# resetting the index to its default
print(df.reset_index(inplace= True))
print(df)

# multi indexes
df.set_index(['Continent','Country'],inplace= True )

# now sorting based from the indexes
df.sort_index(ascending= True)# if you want the next column as well df.sort_index(ascending=[True, False])

# to display more information
pd.set_option('display.max.rows',235)

