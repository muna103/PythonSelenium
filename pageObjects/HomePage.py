from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "div[class='form-group'] input[name='name']")
    email = (By.CSS_SELECTOR, "div[class='form-group'] input[name='email']")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    employment = (By.ID,"inlineRadio2")
    submit = (By.CSS_SELECTOR,"input[type='submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")



    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    def getEmploymnet(self):
        return self.driver.find_element(*HomePage.employment)
    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

