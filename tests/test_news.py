import unittest
from app.models import Article

class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Article('bbc','Independent','Larry Madowo','APIs','Pulling articles through','https://google.com','https://google.com/images','2019-02-02T12:00:00Z','content')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'bbc')
        self.assertEquals(self.new_article.name,'Independent')
        self.assertEquals(self.new_article.author,'Larry Madowo')
        self.assertEquals(self.new_article.title,'Learn APIs')
        self.assertEquals(self.new_article.description,'We are here to learn APIs')
        self.assertEquals(self.new_article.url,'https://yahoo.com')
        self.assertEquals(self.new_article.urlToImage,'https://yahoo.com/images')
        self.assertEquals(self.new_article.publishedAt,'2019-02-04T14:00:00Z')
        self.assertEquals(self.new_article.content,'content')
