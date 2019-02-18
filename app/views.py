from flask import render_template
from app import app
from .models import source
from .request import get_news,get_source
Source=source.Source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # sources=Source.get_source()
    # for source in sources:
    #    source=get_source() 
    #    hhh=get_news(source)  
    sources=get_source()
    print(sources)
    for source in sources:
       source1=get_news(source)
    # bitcoin_news=get_news('bitcoin')
    # tech_news=get_news('TechCrunch')
    # mash_news=get_news('Mashable')
    # cnn_news=get_news('CNN')


    title="Home- News"
    return render_template('index.html', title=title, source1=source1)

@app.route('/article/<article_url>')
def article(article_url):
  '''
  View article page function that article source page
  '''
   