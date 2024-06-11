import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def brawser() -> WebDriver:
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
