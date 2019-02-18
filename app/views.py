from flask import render_template
from app import app
from .models import source
from .request import get_news,get_source
# Source=source.Source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    cat_general = get_source('general')
    cat_business = get_source('business')
    cat_entertainment = get_source('entertainment')
    cat_sports = get_source('sports')
    cat_tech = get_source('technology')
    cat_science = get_source('science')
    cat_health = get_source('health')


    # bitcoin_news=get_news('bitcoin')
    # tech_news=get_news('TechCrunch')
    # mash_news=get_news('Mashable')
    # cnn_news=get_news('CNN')


    title="Home- News"
    # return render_template('index.html', title=title, source1=bitcoin_news,source2=tech_news,source3=mash_news,source4=cnn_news)
    return render_template('index.html',title=title, general=cat_general, business = cat_business, entertainment = cat_entertainment, sports = cat_sports, tech = cat_tech, science = cat_science, health = cat_health)

@app.route('/article/<article_url>')
def article(article_url):
  '''
  View article page function that article source page
  '''
   