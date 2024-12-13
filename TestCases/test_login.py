
import pytest
from configuration import *
from WebPages.LoginPage import Login_Page

@pytest.mark.usefixtures("browser_setup")
class Test_Login:

    # setup_class and teardown_class should be used if no yield defined in configuration browser_setup
    # def setup_class(self):
    #     self.driver.get(base_url)
    #     self.login_page = Login_Page(self.driver)

    def test_validate_login(self):
        self.driver.get(base_url)
        Login_Page(self.driver).login(username, password)
        # self.login_page.login(username,password)

    # def teardown_class(self):
    #     self.driver.quit()