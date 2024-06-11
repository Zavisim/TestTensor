import logging
import time

import pytest


from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.contacts import ContactsPage
from pages.tensor_about import TensorAbout
from pages.tensor_main import TensorMain


@pytest.fixture
def brawser() -> WebDriver:
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def contacts_page(brawser) -> ContactsPage:
    return ContactsPage(brawser)


def test_something(brawser, contacts_page):
    tensor_main = TensorMain(brawser)
    tensor_about = TensorAbout(brawser)

    contacts_page.open()
    contacts_page.banner.click()
    time.sleep(2)
    contacts_page.switch_tab()
    assert brawser.current_url == tensor_main.URL

    assert tensor_main.human_block_title.text == 'Сила в людях'

    tensor_main.cookie_close.click()

    tensor_main.human_block_more_button.click()
    time.sleep(2)
    assert brawser.current_url == tensor_about.URL

    sizes = tensor_about.get_work_block_images_sizes()

    sizes = set(sizes)
    assert len(sizes) == 1


