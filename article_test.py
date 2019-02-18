import unittest
from app.models import article
Article=article.Article

class ArticleTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the article class
  '''

  def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("1234","AKA","Please describe the article","http://coco.thenews","https://kweri.com","12-34-56")

  def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))  

  def test_init_(self):
      '''
      Test to see if article instance are being created
      '''
      self.assertEqual(self.new_article.author,"1234")
      self.assertEqual(self.new_article.title,"AKA")
      self.assertEqual(self.new_article.description,"Please describe the article")
      self.assertEqual(self.new_article.url,"http://coco.thenews")
      self.assertEqual(self.new_article.imageUrl,"https://kweri.com")
      self.assertEqual(self.new_article.publishedAt,"12-34-56")

if __name__ == '__main__':
    unittest.main()            