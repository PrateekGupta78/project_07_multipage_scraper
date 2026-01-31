from bs4 import BeautifulSoup

html = "<h2>   Hello World   </h2>"
soup = BeautifulSoup(html, "html.parser")

print(soup.h2.get_text())
print(soup.h2.get_text(strip=True))