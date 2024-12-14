import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = None
base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
username = "Admin"
password = "admin123"
invalid_psw = "21"

@pytest.fixture(scope="class",autouse=True)
def browser_setup(request):
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield
    request.cls.driver.quit()
