from BasicFunctions.functions import Basic_Functions
from selenium.webdriver.common.by import By

class Login(Basic_Functions):

    username_ele = (By.XPATH,'//input[@name="username"]')
    psw_ele = (By.XPATH,'//input[@name="password"]')
    loginbuttton_ele = (By.XPATH,'//button')

    def __init__(self):
        Basic_Functions.__init__(driver)

    def login(self, username, password):
        self.element_sendkeys(self.username_ele,username)
        self.element_sendkeys(self.psw_ele, password)
        self.element_click(self.loginbuttton_ele)
