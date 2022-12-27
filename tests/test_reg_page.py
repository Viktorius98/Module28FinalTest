from pages.reg_page import RegPage
import time
from selenium.webdriver.common.by import By


def test_contents_reg_page(driver):
    page = RegPage(driver)
    page.link_reg.click()
    page.driver.save_screenshot('Reg_page.png')


def test_firstname_field_reg_page(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('-Иван')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FirstName_Reg_page.png')


def test_firstname_field_rp_2_cor_sym(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('Ив')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FirstName_Reg_page_2sym.png')


def test_firstname_field_rp_15_cor_sym(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('ИваннИваннИванн')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FirstName_Reg_page_15sym.png')


def test_firstname_field_rp_30_cor_sym(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('ИваннИваннИваннИваннИваннИванн')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FirstName_Reg_page_30sym.png')


def test_firstname_field_rp_1_cor_sym(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('И')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FirstName_Reg_page_1sym.png')


def test_firstname_field_rp_31_cor_sym(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('ИваннИваннИваннИваннИваннИваннн')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FirstName_Reg_page_31sym.png')


def test_firstname_field_rp_501_cor_sym(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('ыеспрааааааааааааааааааааааааааааааааааааааровшдуирааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааффффффффффффффффвввввввввввввввввввввввввввввввввввввввввввввваааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FirstName_Reg_page_501sym.png')


def test_firstname_field_rp_china_sym(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('我吃了一个苹果')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.click()
    page.driver.save_screenshot('FirstName_Reg_page_china_sym.png')


def test_lastname_field_reg_page(driver):
    page = RegPage(driver)
    page.link_reg.click()
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('-Иванов')
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.click()
    page.driver.save_screenshot('LastName_Reg_page.png')


def test_email_field_rp(driver):
    page = RegPage(driver)
    page.link_reg.click()
    email = driver.find_element(By.ID, 'address')
    email.clear()
    email.send_keys('bigden76@mail.ru')
    password = driver.find_element(By.ID, 'password')
    password.click()
    page.driver.save_screenshot('Email_Reg_page.png')


def test_pass_field_rp(driver):
    page = RegPage(driver)
    page.link_reg.click()
    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys('Bigden76')
    pass_con = driver.find_element(By.ID, 'password-confirm')
    pass_con.click()
    page.driver.save_screenshot('Pass_Reg_page.png')


def test_pass_con_field_rp(driver):
    page = RegPage(driver)
    page.link_reg.click()
    pass_con = driver.find_element(By.ID, 'password-confirm')
    pass_con.clear()
    pass_con.send_keys('Bigden76')
    password = driver.find_element(By.ID, 'password')
    password.click()
    page.driver.save_screenshot('Pass_con_Reg_page.png')


def test_reg_page_cor_data(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('Иван')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('Иванов')
    email = driver.find_element(By.ID, 'address')
    email.clear()
    email.send_keys('bigden76@mail.ru')
    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys('Bigden76')
    pass_con = driver.find_element(By.ID, 'password-confirm')
    pass_con.clear()
    pass_con.send_keys('Bigden76')
    btn = driver.find_element(By.NAME, 'register')
    btn.click()
    time.sleep(10)
    page.driver.save_screenshot('Registration.png')


def test_reg_page_cor_data2(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('Иван')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('Иванов')
    email = driver.find_element(By.ID, 'address')
    email.clear()
    email.send_keys('bigden76@mail.ru')
    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys('Bigden76')
    pass_con = driver.find_element(By.ID, 'password-confirm')
    pass_con.clear()
    pass_con.send_keys('Bigden76')
    btn = driver.find_element(By.NAME, 'register')
    btn.click()
    time.sleep(10)
    page.driver.save_screenshot('Registration2.png')


def test_reg_page_dif_pass(driver):
    page = RegPage(driver)
    page.link_reg.click()
    firstname = driver.find_element(By.NAME, 'firstName')
    firstname.clear()
    firstname.send_keys('Иван')
    lastname = driver.find_element(By.NAME, 'lastName')
    lastname.clear()
    lastname.send_keys('Иванов')
    email = driver.find_element(By.ID, 'address')
    email.clear()
    email.send_keys('bigden76@mail.ru')
    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys('Bigden76')
    pass_con = driver.find_element(By.ID, 'password-confirm')
    pass_con.clear()
    pass_con.send_keys('Bigden77')
    btn = driver.find_element(By.NAME, 'register')
    btn.click()
    page.driver.save_screenshot('Pass_dif_Reg_page.png')


def test_reg_page_without_data(driver):
    page = RegPage(driver)
    page.link_reg.click()
    btn = driver.find_element(By.NAME, 'register')
    btn.click()
    page.driver.save_screenshot('Without_data_Reg_page.png')


def test_link_ua1_rp(driver):
    page = RegPage(driver)
    page.link_reg.click()
    link_ua1 = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[5]/a')
    link_ua1.click()
    time.sleep(1)
    page.driver.save_screenshot('UA1_reg_page.png')


def test_link_cookie_rp(driver):
    page = RegPage(driver)
    page.link_reg.click()
    cookie = driver.find_element(By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]/span/span')
    cookie.click()
    time.sleep(1)
    page.driver.save_screenshot('cookie_RP.png')


def test_link_cp_rp(driver):
    page = RegPage(driver)
    page.link_reg.click()
    cp = driver.find_element(By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    cp.click()
    time.sleep(1)
    page.driver.save_screenshot('cp_RP.png')


def test_link_ua2_rp(driver):
    page = RegPage(driver)
    page.link_reg.click()
    link_ua2 = driver.find_element(By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]')
    link_ua2.click()
    time.sleep(1)
    page.driver.save_screenshot('UA2_reg_page.png')


def test_link_phone_rp(driver):
    page = RegPage(driver)
    page.link_reg.click()
    phone = driver.find_element(By.XPATH, '//*[@id="app-footer"]/div[2]/a')
    phone.click()
    time.sleep(1)
    page.driver.save_screenshot('Phone_reg_page.png')