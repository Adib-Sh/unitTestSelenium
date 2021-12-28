import unittest
from selenium import webdriver
import page

#PATH = 'C:\Program Files (x86)\chromedriver.exe'
#url = 'http://www.python.org'

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
        self.driver.get("http://www.python.org")
        
    def test_title(self):
        mainpage = page.MainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.search_text_element = 'pycon'
        mainpage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
        unittest.main()
        