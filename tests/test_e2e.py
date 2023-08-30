

import pytest
from selenium.webdriver.support.select import Select

from pageobject.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestOne:
    def teste2e(self):
        homePage=HomePage(self.driver)
        homePage.getName().send_keys("prameela")
        homePage.getEmail().send_keys("abs@gmail.com")
        homePage.getPassword().send_keys("345Prameela")
        db=Select(homePage.getGender())
        db.select_by_index(1)
        homePage.getemployeestatus().click()
        homePage.getdob().send_keys("21-02-2000")
        homePage.SubmitForm().click()
        msg = homePage.getSuccessmsg().text
        print(msg)
