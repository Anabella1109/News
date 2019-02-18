class Article:
   '''
   Article class to define article objects
   '''

   def __init__(self,author,title,description,url,imageUrl,publishedAt):
     self.author=author
     self.title=title
     self.description=description
     self.url=url
     self.imageUrl=imageUrl
     self.publishedAt=publishedAt