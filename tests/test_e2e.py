from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from pageObjects.CheckOutPage import CheckOutPage
import pytest

class TestOne(BaseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)
        homepage.shopItems().click()
       # self.driver.find_element_by_link_text("Shop").click()
        checkoutpage=CheckOutPage(self.driver)
        products = checkoutpage.getproducts()


        #products = self.driver.find_elements_by_css_selector("div[class='card h-100']")

        for product in products:

            productName = product.find_element_by_css_selector("div h4 a").text
           # productName = checkoutpage.getCardTitle()
            if productName == "Blackberry":
                product.find_element_by_css_selector("div[class='card-footer'] button").click()
                self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
        self.driver.find_element_by_css_selector("input[class*='validate filter']").send_keys("ind")
        self.verifyLinkPresence("India")
        #wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_xpath("//a[contains(text(),'India')]").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='checkbox checkbox-primary']")))
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("input[value='Purchase']").click()
        str1 = "Success! Thank you! Your order will be delivered in next few weeks"
        assert str1 in self.driver.find_element_by_css_selector("[class*='alert-success']").text
        self.driver.get_screenshot_as_file("screenshot.png")

