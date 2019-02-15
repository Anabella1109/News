from app import app
import urllib.request,json
from app.models import source,article

Source=source.Source
Article=article.Article
# Getting api key
api_key = app.config['NEWS_API_KEY']

base_url=app.config['NEWS_API_BASE_URL']


def get_news(source):
   '''
   Function that gets the json response to the url request
   '''

   get_news_url=base_url.format(source,api_key)
   with urllib.request.urlopen(get_news_url) as url:
     get_news_data=url.read()
     get_news_response=json.loads(get_news_data)

     news_results=None

     if get_news_response['articles']:
       news_results_list=get_news_response['articles']
       news_results=process_news(news_results_list)

     return news_results

def process_news(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of articles objects
    '''

    news_results=[]
    for article in news_list:
        author=article.get('author')
        title=article.get('title')
        description=article.get('description')
        url=article.get('url')
        imageUrl=article.get('urlToImage')

        if imageUrl:
          article_object=Article(author,title,description,url,imageUrl)
          news_results.append(article_object)
    return news_results    





