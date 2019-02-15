from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    bitcoin_news=get_news('bitcoin')
    tech_news=get_news('TechCrunch')
    mash_news=get_news('Mashable')
    cnn_news=get_news('CNN')


    title="Home- News"
    return render_template('index.html', title=title, source1=bitcoin_news,source2=tech_news,source3=mash_news,source4=cnn_news)

@app.route('/article/<article_url>')
def article(article_url):
  '''
  View article page function that article source page
  '''
   