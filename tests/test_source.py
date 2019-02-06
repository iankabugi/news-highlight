import unittest
from app.models import Source

class SourcesTest(unittest.TestCase):
    '''
    Test case to test the behavior of the Sources class
    '''
    def setUp(self):
        '''
        Setup function that will run before every test
        '''
        self.new_source = Source('CNN','CNN','CNN NEWS','https://yahoo.com','general','english','ke')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        '''
        Test function to check instance variables
        '''
        self.assertEquals(self.new_source.id,'CNN')
        self.assertEquals(self.new_source.name,'CNN')
        self.assertEquals(self.new_source.description,'CNN NEWS')
        self.assertEquals(self.new_source.url,'https://yahoo.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.language,'english')
        self.assertEquals(self.new_source.country,'ke')
