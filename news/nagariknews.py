from .url_open import url_open

def nagarik_crawler(url='http://nagariknews.com/main-story/'):

    '''pull nagariknews.com latest news
       search for the h1 tag which contain news title and url
       fetch the title from h1 tag and the url from the anchor tag 
    '''
    title_and_url = dict()
    data_object = url_open(url)
    data_item = data_object.findAll('h1')

    for news in data_item:
        news = news.findAll('a')
        for newsobj in news:
            news_title = newsobj.get_text()
            news_url = url.split('/main-story/')[0]+ newsobj.get('href')
            title_and_url[news_title] = news_url
    return title_and_url


def nagirak_news_detail(title, url):
    
    '''the url will pass to the url_open object which return the bs4 object
        article body contain two parts intro part and the remaining part
        fetch the text of intro part within the div tag having class of 'itemIntroText'
        again fetch the remaining text of the body which is hold by the div tag
        having class of itemFullText
    '''

    print(title)
    news_object = url_open(url)
    news_intro = news_object.findAll('div', {'class':'itemIntroText'})
    for news_intro_text in news_intro:
        print(news_intro_text.get_text())
    news_body = news_object.findAll('div', {'class':'itemFullText'})
    for divs in news_body:
        print(divs.get_text())
       
if __name__ == '__main__':
    news = nagarik_crawler('http://nagariknews.com/main-story/')
    for title, url in news.items():
        nagirak_news_detail(title, url)
   
