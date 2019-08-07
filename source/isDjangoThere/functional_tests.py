from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Kip Trimmle heard about some online app that makes lists or something
        #S/he goes to check it out
        self.browser.get('http://localhost:8000')
        
        
    
        #title suggests it is a to do list of some manner
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ta\' da', header_text)
        
        # self.assertEqual(
        #    inputbox.get_attribute('placeholder'),
        #    'Enter a to-do item'
        # )
        
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy Item" as an item in a to-do list table
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy Item')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy Item')
        
        # There is still a text box inviting her to add another item. She
        # enters "Use Item"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use Item')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy Item')
        self.check_for_row_in_list_table('2: Use Item')
        
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        
        ##Kippers wonders if site remembers list - sees another text box
        self.fail('finis')
        ##another update
        
if __name__== '__main__':
    unittest.main(warnings='ignore')
browser.quit()  
    

#at the end s/he gets a generated page w/ a unique id

#the next visit, the list is there

