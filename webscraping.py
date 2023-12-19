# first we need to learn about HTMl
# <html>
# <head>
#       <title> My First Web page</title>
# </head>
#
# <body>
# <h1> My first Web page </h1>
# <p><b> Hello World Wide Web </b></p>
# <p><i> Hello World Wide Web </i></p>
# <p><u> Hello World Wide Web </u></p>
# <p> This is my  first Web page </p>
# <p> HTML tags can give <b><i> various</i></b>
# <u>looks and format </u> to the content of this web page.</p>
#
# </body>
# </html>
# scrapping practice website - https://www.scrapethissite.com/pages/forms/

# THE BEGINNERS PACKAGE
#first need to install pip install beautifulsoup4
#requests is another module that needs to be installed if not installed
# from bs4 import BeautifulSoup
# import requests

#100 no data
# 204(no content in the actual web page), 400(invalid no server response ), 401,404(server cannot be found)  potentially bad
# url = 'https://www.scrapethissite.com/pages/forms/'
# page = requests.get(url)
# print(page)

# now copying the html of the site to take a look at it
# soup = BeautifulSoup(page.text,'html')
# print(soup)
# the response is sending the request and the text is retrieving the  raw html we will be using
# the html - is how we will parse the information
# parse -  For programming this is converting information into a format that's easier to work with.

# to make it look pretty when it prints out
# print(soup.prettify())

#FIND AND FIND_ALL - GETTING SPECIFIC INFORMATION
from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)

soup = BeautifulSoup(page.text,'html')
#print(soup)
#print(soup.find('div')) # you can put other tags here, it fetches the first div inthe ex..
#soup.find_all('div') # now this one all div

#breaking it down further
#soup.find_all('div',class_ = 'col-md-12')

# to get  a real information like text
print(soup.find_all('p', class_= 'lead'))
# when you actually want to extract the actual data or text you cannot use find_all
# you have to go back to find since it has that attribute .text
print(soup.find('p', class_ = 'lead').text)
print(soup.find('p', class_ = 'lead').text.strip()) #.strip() to clean it a little bit better


# now we only want to pull out the team name under th(titles of column) - data under the td tag
print(soup.find_all('th'))# columns
print(soup.find_all('td')) # rows

# now to actually do it
print(soup.find('th').text.strip())












