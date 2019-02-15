from app import app
import urllib.request,json
from app.models import source,article

Source=source.Source
Artticle=article.Article
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