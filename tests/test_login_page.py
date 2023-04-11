import time

from pages.data import LoginPageData
from pages.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType


@allure.feature('user_login')
@allure.story('Вводим валидный email и пароль')
@allure.severity('blocker')
def test_go_to_login(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    # page.go_to_login()
    # page.go_to_password()
    page.go_to_login_button()
    time.sleep(3)
    with allure.step('Делаем скриншот'):
        allure.attach(browser.get_screenshot_as_png(), name='result', attachment_type=AttachmentType.PNG)
