from configuration import *
from BasicFunctions.selenium_functions import Functions
from selenium.webdriver.common.by import By

class Login_Page(Functions):

    username_ele = (By.XPATH,'//input[@name="username"]')
    psw_ele = (By.XPATH,'//input[@name="password"]')
    login_buttton_ele = (By.XPATH,'//button')

    # Pay attention to the syntax of inheritance!!!!
    # Never forget to pass self and parameters(e.g. driver) to both __init__()!!!
    def __init__(self, driver):
        Functions.__init__(self, driver)

    def login(self, username, password):
        self.element_sendkeys_until(self.username_ele,username)
        self.element_sendkeys_until(self.psw_ele, password)
        self.element_click_until(self.login_buttton_ele)

