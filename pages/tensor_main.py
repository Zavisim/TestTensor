from selenium.webdriver.common.by import By

from pages.base import BasePage


class TensorMain(BasePage):
    URL = "https://tensor.ru/"

    @property
    def human_block_title(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, '.tensor_ru-Index__block4-content p.tensor_ru-Index__card-title')

    @property
    def cookie_close(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.tensor_ru-CookieAgreement__close')

    @property
    def human_block_more_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content a.tensor_ru-link')
