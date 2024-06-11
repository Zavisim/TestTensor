import time

import pytest
from selenium.webdriver.common.by import By

from pages.base import BasePage


class ContactsPage(BasePage):
    URL = "https://sbis.ru/contacts"

    @property
    def banner(self):
        banner = self.driver.find_element(By.CSS_SELECTOR, 'a.sbisru-Contacts__logo-tensor')
        return banner

    @property
    def region(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')

    @property
    def partners_block(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.sbisru-Contacts-List__name')

    @property
    def change_req(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')

    def change_region(self, region_name):
        self.change_req.click()
        time.sleep(2)
        region = self.driver.find_element(By.CSS_SELECTOR, f'.sbis_ru-Region-Panel__item [title="'
                                                           f'{region_name}"]')
        region.click()
        time.sleep(2)

    def get_partner_names(self) -> list[str]:
        names = []
        for element in self.partners_block:
            names.append(element.text)
        return names

