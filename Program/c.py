Author = 'Liu Lei'

from bs4 import BeautifulSoup

with open('learnn1.html','r') as wb_data:
    Soup=BeautifulSoup(wb_data,'lxml')
    images=Soup.select('body > div.main-content > ul > li > img')
    title=Soup.select('body > div.main-content > h2')
    decs=Soup.select('body > div.main-content > ul > li:nth-of-type(1)>h3')
    '''body > div.main - content > ul > li: nth - child(1) > img
       
        body > div.main-content > ul > li:nth-child(1) > h3
        body > div.main-content > ul > li:nth-child(1) > p
    '''
    for image in images:
        print(image.get_text())
    for titles in title:
        print(titles.get_text())
    for dec in decs:
        print(dec.get_text())