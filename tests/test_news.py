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
        self.new_article = Article('CNN','Independent','Francis T Karagu','APIs','Pulling articles through','https://google.com','https://google.com/images','2019-02-02T12:00:00Z','content')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.name,'Independent')
        self.assertEquals(self.new_article.author,'Francis T Karagu')
        self.assertEquals(self.new_article.title,'APIs')
        self.assertEquals(self.new_article.description,'Pulling articles through')
        self.assertEquals(self.new_article.url,'https://google.com')
        self.assertEquals(self.new_article.urlToImage,'https://google.com/images')
        self.assertEquals(self.new_article.publishedAt,'2019-02-02T12:00:00Z')
        self.assertEquals(self.new_article.content,'content')
