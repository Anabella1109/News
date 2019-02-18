from flask import render_template
from app import app
from .models import source,article
from .request import get_news,get_source
Source=source.Source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_category = get_source('general')
    technology_category = get_source('technology')
    sciences_category = get_source('science')
    entertainment_category = get_source('entertainment')
    sports_category = get_source('sports')
    health_category = get_source('health')
    business_category = get_source('business')



    title="Home- News"
    return render_template('index.html',title=title, general=general_category, business = business_category, entertainment = entertainment_category, sports = sports_category, technology = technology_category, science = sciences_category, health = health_category)

@app.route('/source/<source_name>')
def sources(source_name):
  '''
  View article page function that article source page
  '''

  articles=get_news(source_name)
  title=f'{source_name}'
  return render_template('source.html',title=title,articles=articles)
   