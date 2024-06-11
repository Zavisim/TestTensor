import time


class BasePage:
    URL = None

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(2)

    def switch_tab(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
