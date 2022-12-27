from .base_page import BasePage
from .locators import AuthLocators
import os


class RegPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv('MAIN_URL') or 'https://b2c.passport.rt.ru'
        driver.get(url)
        self.link_reg = driver.find_element(*AuthLocators.AUTH_LINK_REG)