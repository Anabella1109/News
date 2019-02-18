from app import app
import urllib.request,json
from app.models import source,article

Source=source.Source
Article=article.Article
# Getting api key
api_key = app.config['NEWS_API_KEY']

base_url=app.config['NEWS_API_BASE_URL1']
base_url1=app.config['NEWS_API_BASE_URL2']
sources_url=app.config['SOURCES_BASE_URL']



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

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results = process_sources(get_sources_response['sources'])
    
    return sources_results

def process_sources(sources_list):
    '''
    Function that processes the json results
    '''
    sources_results = []

    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        

        if url:
            source_object = Source(id,name,description,url,category)
            sources_results.append(source_object)
    
    return sources_results


       


   






