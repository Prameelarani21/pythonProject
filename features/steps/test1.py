'''from behave import *
from selenium import webdriver

from selenium.webdriver.common.by import By

from main import driver

use_step_matcher("re")

def before_scenario(context,scenario):

    driver=webdriver.Chrome()

def after_scenario(context,scenario):

    if driver:
        driver.quit()

@given("The user is on the registration page")
def step_impl(context):
    driver.get("https://www.facebook.com/login/")

@when("they enter '(?P<email>.+)' and'(?P<password>.+)'")
def step_impl(context, email, password):
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)


@step("they click the login button")
def step_impl(context):
    driver.find_element(By.XPATH,"//button[@value='1']").click()


@then("they should be redirected to the facebook page")
def step_impl(context):
    print(driver.title)'''