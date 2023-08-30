import pytest
from selenium import webdriver
@pytest.fixture()
def setup(request):
    driver=webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    print("Test ended")
    driver.close()
