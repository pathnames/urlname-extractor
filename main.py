from bs4 import BeautifulSoup

with open('5minutes.html') as f: 
    soup = BeautifulSoup(f, 'html.parser')

a_elements  = soup.find_all('a', href = True)

for a in a_elements:
    print(a['href'])