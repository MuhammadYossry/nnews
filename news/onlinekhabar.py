from .url_open import url_open
import re

def onlinekhabar_crawler(url='http://onlinekhabar.com/#tab66'):
    title_and_link = dict()
    data = url_open(url)
    divs = data.findAll('div',{'id':'tab66'})
    for eachdivs in divs:
        links = eachdivs.findAll('a')
        for eachlink in links:
            title = eachlink.get_text()
            link = eachlink.get('href')
            title_and_link[title]=link
        return title_and_link
	

def  onlinekhabar_news_detail(kwargs):
    for title, url in kwargs.items():
        print(title, url)
        raw_data = url_open(url)
        divs  = raw_data.findAll('div', {'id':'sing_cont'})
        for div in divs:
            ptags = div.findAll('p')
            for content in ptags:
                print(content.get_text())
                
    


if __name__ == '__main__':
    url = 'http://onlinekhabar.com/#tab66'
    data = onlinekhabar_crawler(url)
    onlinekhabar_news_detail(data)
