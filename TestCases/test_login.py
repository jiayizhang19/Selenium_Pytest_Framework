import pytest

from configuration import *
from WebPages.LoginPage import Login

@pytest.mark.usefixtures("browser_setup")
class Test_Login:

    def setup_class(self):
        self.driver.get(base_url)
        slef.login_page = Login(self.driver)

    def test_validate_login(self):
        self.login_page.login(username,password)

    def teardown_class(self):
        self.driver.quit()