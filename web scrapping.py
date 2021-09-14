import requests
from bs4 import BeautifulSoup
page=requests.get("https://coronaclusters.in/tamil-nadu")
soup=BeautifulSoup(page.text,'lxml')
d=soup.find('div',attrs={'class':'col-12 card-stats'})
heading_tags = ["h5"]
i=0
for tags in d.find_all(heading_tags):
    if i==0:
        s="Confirmed cases"
    elif i==1:
        s="Active cases"
    elif i==2:
        s="Recovered cases"
    else:
        s="Death count"
    i=i+1
    print(s+" -->  "+tags.text.strip())
    
# to store scrapped data into excel sheet

#import xlrd
#import xlwt
#workbook = xlrd.open_workbook("D:\\indhu college\\miniproject-2\\covid\\tamilnadu.xls")
#workbook = xlwt.Workbook()
#sheet = workbook.add_sheet('test')
#sheet.write(3,3,"indhu")
