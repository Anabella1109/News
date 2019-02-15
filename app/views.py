from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title="Home- News"
    return render_template('index.html', title=title)

@app.route('/article/<article_url>')
def article(article_url):
  '''
  View article page function that article source page
  '''
   