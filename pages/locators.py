from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_EMAIL = (By.ID, 'username')
    AUTH_PASS = (By.ID, 'password')
    AUTH_BTN = (By.ID, 'kc-login')
    AUTH_LINK_UA1 = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/a')
    AUTH_LINK_VK = (By.ID, 'oidc_vk')
    AUTH_LINK_OK = (By.ID, 'oidc_ok')
    AUTH_LINK_MAIL = (By.ID, 'oidc_mail')
    AUTH_LINK_GOOGLE = (By.ID, 'oidc_google')
    AUTH_LINK_YA = (By.ID, 'oidc_ya')
    AUTH_LINK_REG = (By.ID, 'kc-register')
    AUTH_LINK_COOKIE = (By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]/span/span')
    AUTH_LINK_CP = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    AUTH_LINK_UA2 = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]')
    AUTH_LINK_PHONE = (By.XPATH, '//*[@id="app-footer"]/div[2]/a')


class RegLocators:
    REG_FIRST_NAME = (By.NAME, 'firstName')
    REG_LAST_NAME = (By.NAME, 'lastName')
    REG_EMAIL_OR_NUMBER = (By.ID, 'address')
    REG_PASS = (By.ID, 'password')
    REG_PASS_CON = (By.ID, 'password-confirm')
    REG_BTN = (By.NAME, 'register')
    REG_LINK_UA1 = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[5]/a')
    REG_LINK_COOKIE = (By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]/span/span')
    REG_LINK_CP = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    REG_LINK_UA2 = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]')
    REG_LINK_PHONE = (By.XPATH, '//*[@id="app-footer"]/div[2]/a')