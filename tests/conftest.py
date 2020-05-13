import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path='F:\\chromedriver.exe')

    elif browser_name=="firefox":
        driver = webdriver.Firefox(executable_path='F:\geckodriver.exe')

    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path='F:\IEDriverServer.exe')

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
