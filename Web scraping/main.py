# This is the Code of the How to scrap the Particular website 

# This is something we have to install throught  the terminal
# pip install requests
# pip install bs4 (beautifulsoup4)
# pip install html5lib

# The purpose of the html5lib is to understand the html code from the web page and parse the html code in the given tags and attribute 


import requests 
from bs4 import BeautifulSoup

url="https://interncrowd.in/index.html"
# Here We have to use the get method for the getting data from the HTML page 
# There are two types of the method post and get 
data = requests.get(url)
htmlcontent = data.content
# This print Statment give the code of particular website in the string format 
# print(htmlcontent)


# For the parse the  string code 
soup = BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify())


# This is the line of the code for the getting the title of the HTML page 
title=soup.title
# print(title)
# print(type(title))

# This is the line to get all the paragraphs from the HTML  page 

paras = soup.find_all('p')
# print(paras)



# This is the line of the code for printing the all anchor tag

anchors = soup.find_all('a')
# print(anchors)




# This is the line of the code to get the first element of the HTML page 


# print(soup.find('p'))


# print(soup.find('p')['class'])

# This is the code to get the all the paargraph which having the class as
 
# print(soup.find_all('p',class_=''))


# This is the line of the code to get the text 
# when we have to print only the text from the paragraph


# print(soup.find('p').get_text())



# This is the actully the code to get the string from the Web page 

# class1 = soup.find(id='imgpreview2')
# print(class1)

# for x in class1.strings :
#     print(x)


# Take the website url which having atleast one element have the attribute ID 
class1 = soup.find(id='')
# print(class1)

# for x in class1.stripped_strings :
#     print(x)
    
# This is the code for getting the next sibling of the div tag 

# print(class1.next_sibling)

# This is the code to get the previous sibling of the div tag 

# print(class1.previous_sibling)
    

# This is the code to get the all link of the web page 

# class2= soup.find_all('a')

# for link in class2 :
#     print(link.get('href'))


# class3=soup.find_all
# print(class3)


