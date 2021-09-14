import requests
from bs4 import BeautifulSoup
page=requests.get("https://www.tooloogle.com/coronavirus-statistics/india/Tamil%20Nadu")
soup=BeautifulSoup(page.text,'lxml')
d=soup.find("div",attrs={"class":"table-responsive"})

print(d)
'''r= d.tbody.find_all("tr")  # contains 2 rows

# Get all the headings of Lists
headings = []
for td in r[0].find_all("td"):
    # remove any newlines and extra spaces from left and right
    headings.append(td.b.text.replace('\n', ' ').strip())
print(headings)'''

