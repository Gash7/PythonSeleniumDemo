from selenium import webdriver
from POMdemo.new_locators.locators import Locator
class Login_Page():
    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_id = Locator.username_textbox_id
        self.password_textbox_id = Locator.password_textbox_id
        self.login_button_id = Locator.login_button_id

    def username(self,uname):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        #username = int(uname)
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(uname)

    def password(self,pword):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(pword)

    def login(self):
        self.driver.find_element_by_id('u_0_2').click()
