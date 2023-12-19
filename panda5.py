# merge,join and concatenate data frames
# how = 'inner'  natural join - what they have in common
# how = 'outer'  full outer join-all the data
# how = 'left'  left outer join- everything from the left and anything similar
# how = 'right'  right outer join- everything from the right and anything similar

import pandas as pd
df1 = pd.read_csv(r'C:\Users\HP\Downloads\LOTR.csv')
df2 = pd.read_csv(r'C:\Users\HP\Downloads\LOTR 2.csv')
print(df1)
print(df2)

# merge, the most basic
#df1.merge(df2)- which would be the same as below #2
# the first one is the left the second one is the right
#without specifying you will get an inner join
# print(df1.merge(df2,how = 'inner',on ='FellowshipID')) #1
# print(df1.merge(df2,how = 'inner',on =['FellowshipID','FirstName'])) #2


#outer- note - the NAN - not a number - means it did not find a match to another column in the opposite table.
#print(df1.merge(df2, how = 'outer'))

#another one is a cross join
#it compares the value from the left df and the right df literaly
df1.merge(df2, how= 'cross')


#JOIN SIMILAR TO MERGE BUT MORE COMPLEX but better when working with INDEXES.
#df1.join(df2) # this doesn't work,you need to specify it like below
#print(df1.join(df2, on= 'FellowshipID',how = 'outer', lsuffix = 'Left',rsuffix = 'Right' ))
# output
#     FellowshipID  FellowshipIDLeft  ... FirstNameRight     Age
# 0.0          1001            1001.0  ...            NaN     NaN
# 1.0          1002            1002.0  ...            NaN     NaN
# 2.0          1003            1003.0  ...            NaN     NaN
# 3.0          1004            1004.0  ...            NaN     NaN
# NaN             0               NaN  ...          Frodo    50.0
# NaN             1               NaN  ...        Samwise    39.0
# NaN             2               NaN  ...        Legolas  2931.0
# NaN             3               NaN  ...         Elrond  6520.0
# NaN             4               NaN  ...       Barromir    51.0
#
# [9 rows x 7 columns]


# now to actually use the join with indexes
df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'),lsuffix = 'Left',rsuffix = 'Right')
print(df4)
# output
#              FirstNameLeft     Skills FirstNameRight   Age
# FellowshipID
# 1001                 Frodo     Hiding          Frodo  50.0
# 1002               Samwise  Gardening        Samwise  39.0
# 1003               Gandalf     Spells            NaN   NaN
# 1004                Pippin  Fireworks            NaN   NaN

# note we can still specify how they are join by this
df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'),lsuffix = 'Left',rsuffix = 'Right',how= 'outer')


#CONCATENATE LIKE PUTING DF ON TOP OF EACH OTHER NOT LIKE JOIN OR MERGE NEXT TO EACH OTHER
con = pd.concat([df1,df2])
print(con)

# Output
#  FellowshipID FirstName     Skills     Age
# 0          1001     Frodo     Hiding     NaN
# 1          1002   Samwise  Gardening     NaN
# 2          1003   Gandalf     Spells     NaN
# 3          1004    Pippin  Fireworks     NaN
# 0          1001     Frodo        NaN    50.0
# 1          1002   Samwise        NaN    39.0
# 2          1006   Legolas        NaN  2931.0
# 3          1007    Elrond        NaN  6520.0
# 4          1008  Barromir        NaN    51.0

# you can still use inner join here
innerconcate = pd.concat([df1,df2],join = 'inner')
print(innerconcate)

outer = pd.concat([df1,df2],join = 'outer', axis = 1)
print (outer)
# axis 0” represents rows and “axis 1” represents columns.
#  FellowshipID FirstName     Skills     Age
# 0          1001     Frodo     Hiding     NaN
# 1          1002   Samwise  Gardening     NaN
# 2          1003   Gandalf     Spells     NaN
# 3          1004    Pippin  Fireworks     NaN
# 0          1001     Frodo        NaN    50.0
# 1          1002   Samwise        NaN    39.0
# 2          1006   Legolas        NaN  2931.0
# 3          1007    Elrond        NaN  6520.0
# 4          1008  Barromir        NaN    51.0
#output at axis = 1
# FellowshipID FirstName     Skills  FellowshipID FirstName   Age
# 0        1001.0     Frodo     Hiding          1001     Frodo    50
# 1        1002.0   Samwise  Gardening          1002   Samwise    39
# 2        1003.0   Gandalf     Spells          1006   Legolas  2931
# 3        1004.0    Pippin  Fireworks          1007    Elrond  6520
# 4           NaN       NaN        NaN          1008  Barromir    51

# The append data frame is use to append rows from one dataframe to the end of another df
df1.append(df2) # note this is the old way the new way is concat




















