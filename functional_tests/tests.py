from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
        
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:  
            try:
                table = self.browser.find_element_by_id('id_list_table')  
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > MAX_WAIT:  
                    raise e  
                time.sleep(0.5)  
                
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn(row_text, [row.text for row in rows])
                
    def test_can_start_a_list_for_one_user(self):
        #Kip Trimmle heard about some online app that makes lists or something
        #S/he goes to check it out
        self.browser.get(self.live_server_url)                
    
        #He notices the page title suggests it is a to do list of some manner
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('todo', header_text)
        
        # kip is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
                
        # he types "Buy Item" into a text box
        inputbox.send_keys('Buy Item')
         
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy Item" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Item')             
                
        # There is still a text box inviting her to add another item. She
        # enters "Use Item"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use Item')
        inputbox.send_keys(Keys.ENTER)
               
        # The page updates again, and now shows both items on the list
        self.wait_for_row_in_list_table('2: Use Item')
        self.wait_for_row_in_list_table('1: Buy Item')        
          

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Kip starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy Item')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Item')
        
        #Mr Trimmle notes his list has a unique URL
        kip_list_url = self.browser.current_url
        self.assertRegex(kip_list_url, '/lists/.+')
        
        # A new user, Count Dracula, visits site.
        #we use new browser session to separate info
        #no info is coming through from cookies, etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        # The Count visits the home page, no sign of Kips list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy Item', page_text)
        self.assertNotIn('make', page_text)
        
        # The Count starts a new list by entering a new item. He is 
        #less...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy Blood')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Blood')
        
        # Drac gets his own unitque URL
        dracula_list_url = self.browser.current_url
        self.assertRegex(dracula_list_url, '/lists/.+')
        self.assertNotEqual(dracula_list_url, kip_list_url)
        
        #no trace of Kip's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy now', page_text)
        self.assertIn('Buy Blood', page_text)
        ##Kippers wonders if site remembers list - sees another text box
        ##self.fail('finis')
        ##another update        

###below code can be used to execute functional tests - commented out because Django is handling it
# if __name__== '__main__':
    # unittest.main(warnings='ignore')
# browser.quit()  
    

#at the end s/he gets a generated page w/ a unique id

#the next visit, the list is there

