from pages.auth_page import AuthPage
import time


def test_contents_auth_page(driver):
    page = AuthPage(driver)
    page.driver.save_screenshot('Auth_page.png')


def test_link_ua1(driver):
    page = AuthPage(driver)
    page.link_ua1.click()
    time.sleep(1)
    page.driver.save_screenshot('UA1_page.png')


def test_link_vk(driver):
    page = AuthPage(driver)
    page.link_vk.click()
    page.driver.save_screenshot('VK_page.png')


def test_link_ok(driver):
    page = AuthPage(driver)
    page.link_ok.click()
    page.driver.save_screenshot('OK_page.png')


def test_link_mail(driver):
    page = AuthPage(driver)
    page.link_mail.click()
    page.driver.save_screenshot('Mail_page.png')


def test_link_google(driver):
    page = AuthPage(driver)
    page.link_google.click()
    page.driver.save_screenshot('Google_page.png')


def test_link_ya(driver):
    page = AuthPage(driver)
    page.link_ya.click()
    page.driver.save_screenshot('Ya_page.png')


def test_link_cookie(driver):
    page = AuthPage(driver)
    page.link_cookie.click()
    page.driver.save_screenshot('Cookie.png')


def test_link_cp(driver):
    page = AuthPage(driver)
    page.link_cp.click()
    time.sleep(1)
    page.driver.save_screenshot('CP_page.png')


def test_link_ua2(driver):
    page = AuthPage(driver)
    page.link_ua2.click()
    time.sleep(1)
    page.driver.save_screenshot('UA2_page.png')


def test_link_phone(driver):
    page = AuthPage(driver)
    page.link_phone.click()
    driver.get_screenshot_as_file('Phone.png')


def test_auth_with_correct_data(driver):
    page = AuthPage(driver)
    page.enter_email('viksin376@yandex.ru')
    page.enter_pass('Ghjrnjk76')
    page.btn_click()
    time.sleep(3)
    page.driver.save_screenshot('User_page.png')


def test_auth_with_incorrect_email(driver):
    page = AuthPage(driver)
    page.enter_email('bigden7@mail.ru')
    page.enter_pass('Bigden76')
    page.btn_click()
    page.driver.save_screenshot('Incorrect_email.png')


def test_auth_with_incorrect_pass(driver):
    page = AuthPage(driver)
    page.enter_email('bigden76@mail.ru')
    page.enter_pass('Bigden766')
    page.btn_click()
    page.driver.save_screenshot('Incorrect_pass.png')


def test_link_reg(driver):
    page = AuthPage(driver)
    page.link_reg.click()
    page.driver.save_screenshot('Reg_page.png')