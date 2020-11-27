import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class HackerNewsSearchTest(unittest.TestCase):
    def setUp(self):
        caps = {'browserName': 'firefox'}
        time.sleep(5)
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )
    def test_hackernews_search_for_testdrivenio(self):
        browser = self.browser
        browser.get("http://www.python.org")
        assert "Python" in browser.title
        elem = browser.find_element_by_name("q")
        elem.send_keys("documentation")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in browser.page_source
    def test_hackernews_search_for_title(self):
        browser = self.browser
        browser.get("http://www.python.org")
        print("browser title=",browser.title)
        assert "Python" in browser.title
    def test_hackernews_search_for_cururl(self):
        browser = self.browser
        browser.get("http://www.python.org")
        print("browser title=",browser.current_url)
        assert "python" in browser.current_url

    def test_hackernews_search_for_selenium(self):
        browser = self.browser
        browser.get('https://news.ycombinator.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('selenium')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('selenium', browser.page_source)
    def tearDown(self):
        self.browser.quit()  # quit vs close?


if __name__ == '__main__':
    unittest.main()