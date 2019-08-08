import unittest
import time
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from selenium import webdriver
from POMdemo.new_page.login_page import Login_Page

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\Selenium\chromedriver_win32\chromedriver.exe')
        cls.driver.implicitly_wait(20)

    def test_page(self):
        driver = self.driver
        driver.get('https://www.facebook.com')
        page = Login_Page(driver)
        page.username("Username")
        page.password('Password')
        # page.username_textbox_id("9890449707")
        # page.password_textbox_id("Ashu@022")
        page.login()

        # self.driver.find_element_by_id('email').send_keys('9890449707')
        # self.driver.implicitly_wait(20)
        # self.driver.find_element_by_id('pass').send_keys('Ashu@022')
        # self.driver.find_element_by_id('u_0_2').click()
        # self.driver.set_script_timeout(7)

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.implicitly_wait(10)
        time.sleep(5)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'),verbosity=2)
