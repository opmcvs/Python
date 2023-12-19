import pandas as pd
# for csv importation - note pandas calls it in as a data frame
read_file =  pd.read_csv(r"C:\Users\HP\Documents\countries of the world.csv")
#print(read_file)
# to remove the headers in the file , the headers will be replace with indexes start from 0
read_file = pd.read_csv(r"C:\Users\HP\Documents\countries of the world.csv", header = None)

# now to put a name to the headers# take note of the r inside the ()
df = pd.read_csv(r"C:\Users\HP\Documents\countries of the world.csv", header = None, names=['Country','Region'])

# if the above file is a txt file , but not the proper way
#df1 = pd.read_csv(r"C:\Users\HP\Documents\countries of the world.txt",sep = '\t' )

# the proper way is changing csv to table for txt file
#df1 = pd.read_table(r"C:\Users\HP\Documents\countries of the world.txt" )

#json files
dfj = pd.read_json(r'C:\Users\HP\Downloads\json_sample.json')
#print(dfj)

#excel files with two sheets in one workbook
#dfe = pd.read_excel(r'C:\Users\HP\Downloads\world_population_excel_workbook.xlsx')
#print(dfe)

# now to specify the sheet name in this case two the first one is world_population the 2nd is Sheet1
dfe1 = pd.read_excel(r'C:\Users\HP\Documents\world_population_excel_workbook.xlsx', sheet_name='Sheet1')
#print(dfe1)
dfe2 = pd.read_excel(r'C:\Users\HP\Documents\world_population_excel_workbook.xlsx', sheet_name='Sheet1',header=None,names=['some','name'])
# print(dfe2)
# from the above having error
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# this means we have to update the xlrd library
# you can do so by py -m pip install --upgrade xlrd


# to change how the data is being displayed from 234 rows X 4 columns  and the ........
# we are basically changing the rows

pd.set_option('display.max.rows',235)
#pd.set_option('display.max.columns',40) - for columns

# to get a little bit of data
print(dfe2.info())
# MultiIndex: 235 entries, ('Rank', 'CCA3') to (74, 'ZWE')
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   some    235 non-null    object
#  1   name    235 non-null    object
# dtypes: object(2)
# memory usage: 24.5+ KB

# just to know the rows and columns total number
print(dfe2.shape)

# to take a peak of the first values (10) can be any number you need to look at.
# print(dfe2.head(10))
# print(dfe2.tail(10)) # for the bottom

# if we don't want to look at all the values or columns
#print(dfe2.columns)
#print(dfe2.rows) - this command doesn't exist
# print(dfe2['some']) # this represents the first column change from Country to some , it doesn't affect the rank or cca3 which seems to be indexes


# to look for a particular data  if you know the first col data
#Rank	CCA3	Country	Capital this is the column the 224 is base on the data in the first column not the index location.

#print(dfe2.loc[224]) - for the that data in a row

# to look for a data based on the integer(index location )
#print(dfe2.iloc[224])- for the index not based on the data itself.