from bs4 import BeautifulSoup

html_file = open("generic_simple.html", mode='r', encoding="utf-8")
html_lido = html_file.read()
soup = BeautifulSoup(html_lido, 'html.parser')

print(soup.prettify())
print(soup.title)
print(soup.title.string)

for i in list(soup.div.children):
    print(i.name)
print(soup.find("div"))
