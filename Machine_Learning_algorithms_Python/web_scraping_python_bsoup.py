#Importing required libraries for scraping.

import urllib2

#Specifying the URL

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#Query the website and return the html to the variable 'page'

page = urllib2.urlopen(wiki)

#Import the beautiful soup functions to parse the data returned from the website.

from bs4 import BeautifulSoup

#Parse the HTML in the 'page' variable and store it in a beautiful soup format.

soup = BeautifulSoup(page)

#soup =  soup.prettify()

print soup.title

print soup.title.string

print soup.a

all_links = soup.find_all("a")

print all_links

for link in all_links:
    print link.get("href")

all_tables = soup.find_all('table')
 
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')

print right_table

