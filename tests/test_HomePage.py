import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " +getData["firstName"])
        homepage.getName().send_keys(getData["firstName"])
        homepage.getEmail().send_keys(getData["lastName"])
        self.selectOptionByText(homepage.getGender(),getData["gender"])
        homepage.getSubmit().click()
        alertText = homepage.getSuccessMessage().text
        assert "Success" in alertText
        self.driver.refresh()


    @pytest.fixture(params=HomePageData.getTestdata("testCase2"))
    def getData(self, request):
        return request.param
