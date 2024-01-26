#!/usr/bin/python3
"""
Python web scrapping using beautifulSoup
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

# consider the following html file string
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')
print(soup.prettify())

#### For simplicity, I will avoid assigning the BeautifulSoup objects to variables and just print them

# how to get a tag eg. a title tag
print(soup.title)

# how to get it's content "the string"
print(soup.title.text)

# the tags object type
print(type(soup.title))

# if there is more than one tag with the same name, the first one is called.
print(soup.h3)

# we can navigate deeper in the tree to the <b> tag.
print(soup.h3.b)

# how to navigate back up to the parent of a tag
soup_obj = soup.h3.b
print(soup_obj.parent)

# and even farther back up the tree
print(soup_obj.parent.parent)

# how to navigate to siblings of a tag
print(soup.h3.next_sibling)

# To get a tags attributes, e.g the class, id, etc, you can treat the tag as a dictionary and the attribute as the key to get it's value
print(soup.h3.b['id'])

# You can also access all the attributes in form of a python dict as attrs
print(soup.h3.b.attrs)

# Also, you can get the content of an attribute using the get() method
print(soup.h3.b.get('id'))

#### NAVIGABLE STRING
# a string corresponds to a bit of text content within a tag.
# we can use the .string attribute to get it
print(soup.h3.b.string)
# checking if the type is a navigable string
print(type(soup.h3.b.string))
# the main difference of navigablestring and a regular python string is that
# it supports some BeautifulSoup features

# we can convert it to a regular string using the str() method
nv_str = soup.h3.b.string
str_nv_str = str(nv_str)
print(type(str_nv_str))

###### FILTER

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, 'html5lib')
table_row = table_bs.find_all('tr')
print(table_row)
print(table_row[0])

# Iterating through the table rows

for i, row in enumerate(table_row):
    print('row: ', i, row)

# Iterating through all the table cells

for i, row in enumerate(table_row):
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print('column:', i, 'cell:', j, cell)

# To match against multiple items we can use a list as the parameter

list_input = table_bs.find_all(['tr', 'td'])
print(list_input)

# Using attributes to filter tags with the find_all() method. e.g the id attribute.
# It returns a list of them
print(table_bs.find_all(id="flight"))

# We can find all the elements that have links to the Florida Wikipedia page
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(list_input)

# If we set the href attribute to true, all tags with a href attribute will be returned
# no matter what the link is.

print(table_bs.find_all(href=True))

# We can also use the string argument to get the tags with a given string

print(table_bs.find_all(string='Florida'))



### FIND

# we can use the find() method to scan the whole document. it returns the first occurence of the argument.
# consider this html doc

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

two_tables_bs = BeautifulSoup(two_tables, 'html.parser')

# We can find the first table using the tag name table

print(two_tables_bs.find('table'))

# We can filter on the class attribute to find the second table which has the class "pizza"

#two_tables_bs.find("table",class='pizza') # throwing an error because of the word class


# DOWNLOADING AND SCRAPING THE CONTENTS OF A WEB PAGE

url = 'https://www.ibm.com'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')

# Scrape all links
for link in soup.find_all('a', href=True):
    print(link.get('href'))

#scrape all images
for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))



#### SCRAPING TABLES FROM A WEB PAGE USING PANDAS
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

tables = pd.read_html(url)
print(tables)








