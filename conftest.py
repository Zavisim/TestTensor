import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.contacts import ContactsPage


@pytest.fixture
def browser() -> WebDriver:
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def contacts_page(browser) -> ContactsPage:
    return ContactsPage(browser)
