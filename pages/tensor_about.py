from selenium.webdriver.common.by import By

from pages.base import BasePage


class TensorAbout(BasePage):
    URL = "https://tensor.ru/about"

    @property
    def work_block_images(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.tensor_ru-About__block3-image')

    def get_work_block_images_sizes(self):
        sizes = []
        for i in self.work_block_images:
            size_dict = i.size
            sizes.append((size_dict['height'], size_dict['width']))
        return sizes
