import logging
import time
import pytest


from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.contacts import ContactsPage


def test_contacts_page_change_region(browser, contacts_page):
    contacts_page.open()
    time.sleep(2)
    assert contacts_page.region.text == 'Ярославская обл.'
    old_partners = contacts_page.get_partner_names()
    assert len(old_partners) > 0

    contacts_page.change_region('Камчатский край')

    assert contacts_page.region.text == 'Камчатский край'

    new_partners = contacts_page.get_partner_names()

    assert old_partners != new_partners
    assert '41-kamchatskij-kraj' in browser.current_url
    assert 'Камчатский край' in browser.title





