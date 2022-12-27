from .base_page import BasePage
from .locators import AuthLocators
import os


class AuthPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv('MAIN_URL') or 'https://b2c.passport.rt.ru'
        driver.get(url)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.link_ua1 = driver.find_element(*AuthLocators.AUTH_LINK_UA1)
        self.link_vk = driver.find_element(*AuthLocators.AUTH_LINK_VK)
        self.link_ok = driver.find_element(*AuthLocators.AUTH_LINK_OK)
        self.link_mail = driver.find_element(*AuthLocators.AUTH_LINK_MAIL)
        self.link_google = driver.find_element(*AuthLocators.AUTH_LINK_GOOGLE)
        self.link_ya = driver.find_element(*AuthLocators.AUTH_LINK_YA)
        self.link_reg = driver.find_element(*AuthLocators.AUTH_LINK_REG)
        self.link_cookie = driver.find_element(*AuthLocators.AUTH_LINK_COOKIE)
        self.link_cp = driver.find_element(*AuthLocators.AUTH_LINK_CP)
        self.link_ua2 = driver.find_element(*AuthLocators.AUTH_LINK_UA2)
        self.link_phone = driver.find_element(*AuthLocators.AUTH_LINK_PHONE)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()