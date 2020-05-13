from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.CSS_SELECTOR, "div[class='card h-100']")
    cardTitle = (By.CSS_SELECTOR, "div h4 a")


    def getproducts(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)



