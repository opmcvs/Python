#Data cleaning in Pandas
# import pandas as pd
# df = pd.read_excel(r'C:\Users\HP\Downloads\Customer Call List.xlsx')
# #print(df)
# # 1st usually is to eliminate the duplicates
# df = df.drop_duplicates() # so that the changes would be saved by placing in a variables
# # or by using inplace = True
# # ex. df.drop(columns = 'Not_Useful_Column ',inplace = True)
#
# #2 then we drop the columns that we don't need
# # in this case we want the Not_Useful_Column - Deleted
# df.drop(columns = 'Not_Useful_Column ')
#
#
# #3 Now we are fixing the LastName as there are /,. NaN
# df['LastName'].str.strip() # by default removes the white spaces only so we need to specify
# df['LastName'] = df['LastName'].str.lstrip('...') # so that it will save only in the column of LastName
# df['LastName'] = df['LastName'].str.lstrip('/')
# df['LastName'] = df['LastName'].str.rstrip('_')
#
# # Below is same thing as above
# df['LastName'] = df['LastName'].str.strip('123._/')# take note the 123 = numbers
#
# # Arranging the phone numbers they should like this = 123-545-5421
# df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-z A-z 0-9]', '')
# # ^ this is called a carrot- meaning return all values except
# print(df)

import pandas as pd
df = pd.read_excel(r'C:\Users\HP\Downloads\Customer Call List.xlsx')
print(df)
df = df.drop_duplicates()
print(df)
print(df.columns)

df = df.drop(columns='Not_Useful_Column')
print(df)
print(df['Last_Name'])
df['Last_Name']= df['Last_Name'].str.strip('123._/')
print(df['Last_Name'])

