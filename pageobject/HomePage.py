from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.XPATH,"//label[text()='Name']/following-sibling::input")
    email = (By.NAME,"email")
    password = (By.ID,"exampleInputPassword1")
    chechbox = (By.ID,"exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    employeestatus=(By.ID,"inlineRadio2")
    dob = (By.XPATH,"//input[@type='date']")
    submit = (By.XPATH,"//input[@type='submit']")
    successmsg = (By.XPATH,"//div[contains(@class,'alert')]")

    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)
    def getCheckbox(self):
        return self.driver.find_element(*HomePage.chechbox)
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    def getemployeestatus(self):
        return self.driver.find_element(*HomePage.employeestatus)
    def getdob(self):
        return self.driver.find_element(*HomePage.dob)
    def SubmitForm(self):
        return self.driver.find_element(*HomePage.submit)
    def getSuccessmsg(self):
        return self.driver.find_element(*HomePage.successmsg)




