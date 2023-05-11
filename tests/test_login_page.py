import time

from pages.data import LoginPageData
from pages.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType


@allure.feature('user_login')
@allure.story('Вводим валидный email и пароль')
@allure.severity('blocker')
def test_go_to_login(browser): # Тестируем логин в системе с валидными данными
    with allure.step("Testing successful login"):
        link = LoginPageData.LOGIN_PAGE_URL
        page = LoginPage(browser, link)
        page.open()
        # page.go_to_login()
        # page.go_to_password()
        page.go_to_login_button()
        time.sleep(3)

    # Ожидаемый результат
    #
    # with allure.step("Проверяем текущий url"):
    #     current_url = browser.current_url
    #     print(current_url)
    #     assert'dashboards/analytics' in current_url, f"current_url doesn't content 'dashboards/analytics'"

    with allure.step('Делаем скриншот'):
        allure.attach(browser.get_screenshot_as_png(), name=r'C:\Users\DELL\PycharmProjects\AntHill\results',
                      attachment_type=AttachmentType.PNG), "Скриншот не создан"

# Run test:
#pytest .\tests\test_login_page.py --alluredir results