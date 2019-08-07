from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ta\' da', header_text)
        
        ##s/he is invited to make one, and does so
        inputbox = self.browser.find_element_by_id('id_new_item')
        # self.assertEqual(
            # inputbox.get_attribute('placeholder'),
            # 'Enter a to-do item'
        # )
        
        inputbox.send_keys('Buy Item')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        #page updates automatically as items are added
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy Item', [row.text for row in rows])
        elf.assertIn('2: Use Item', [row.text for row in rows])
        ##Kippers sees another text box
        self.fail('finis')
        ##another update
        
if __name__== '__main__':
    unittest.main(warnings='ignore')
browser.quit()  
    

#at the end s/he gets a generated page w/ a unique id

#the next visit, the list is there

