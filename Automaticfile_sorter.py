# if you have different data types in one folder like png, csv, text file
# and go into their own folder without the drag and drop
# filesortertest is the name of our test folder
# shutil- perform high level operations for files in file explorer
# os -provides functions for interacting with the operating system

# so you have to create a folder check the files then place them on the right folder

import os,shutil
path = r"C:/Users/HP/Documents/filesortertest/" # take note of the slash from \ to / for creating purposes
#print(os.listdir(path)) # to show all the files
# if you get SYNTAXERROR - EOL while scanning string literal - you need to change the \ to / all and add in the end/
# now to check if the file exists
file_not_included = False;
folder_names = ['csv/xlsx files','images files','text files','word file']
for loop in range(1,4): # it doesn't count from 0
  if not os.path.exists(path + folder_names[loop]):
      os.makedirs(path + folder_names[loop])

# now to put the files in the right folder
file_name = os.listdir(path)
for file in file_name:
    if '.xlsx' in file and not os.path.exists(path+ 'csv/xlsx files/'+file):
        shutil.move(path+ file,path +'csv/xlsx files/'+file )
    elif '.PNG' in file and not os.path.exists(path+ 'images files/'+file):
        shutil.move(path+ file,path +'images files/'+file )
    elif '.txt' in file and not os.path.exists(path+ 'text files/'+file):
        shutil.move(path+ file,path +'text files/'+file )
    elif '.docx' in file and not os.path.exists(path+ 'word file/'+file):
        shutil.move(path+ file,path +'word file/'+file )
    else:
       file_not_included = True
if file_not_included:
    print('This file is not included')




