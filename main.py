from bs4 import BeautifulSoup

with open('5minutes.html') as f: 
    soup = BeautifulSoup(f, 'html.parser')

a_elements  = soup.find_all('a', href = True)
text_to_url = {}

for a in a_elements:
    text_to_url[a.getText()] = a['href']

print(text_to_url)