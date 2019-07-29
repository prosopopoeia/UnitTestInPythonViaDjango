from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Kip Trimmle heard about some online app that makes lists or something
        #S/he goes to check it out
        self.browser.get('http://localhost:8000')
        
        
    
        #title suggests it is a to do list of some manner
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the spinach!")
        
        ##s/he is invited to make one, and does so
        #page updates automatically as items are added
        
if __name__== '__main__':
    unittest.main(warnings='ignore')
    

#at the end s/he gets a generated page w/ a unique id

#the next visit, the list is there

browser.quit()  