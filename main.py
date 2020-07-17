from bs4 import BeautifulSoup

with open('5minutes.html') as f: 
    soup = BeautifulSoup(f, 'html.parser')

print(soup)