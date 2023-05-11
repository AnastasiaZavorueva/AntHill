import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType
from pages.data import WikiPageData
from pages.wiki_creation_page import WikiCreationPage


@allure.feature('Wiki_creation')
@allure.story('Создаем wiki пространство')
@allure.severity('blocker')
def test_wiki_creation(browser, go_to_login):
    link = WikiPageData.WIKI_PAGE_URL
    page = WikiCreationPage(browser, link)
    page.open()
    page.click_create_button()
    # time.sleep(3)
    # browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_login.png')
    page.choose_logo()
    # time.sleep(3)
    # browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_logo.png')
    page.enter_title()
    # time.sleep(3)
    # browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_title.png')
    page.enter_description()
    # time.sleep(3)
    # browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_description.png')
    page.enter_category()
    # time.sleep(3)
    # browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_category.png')
    page.add_button()
    time.sleep(3)
    # browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_add.png')

    # Ожидаемый результат

    with allure.step("Проверяем текущий url"):
        current_url = browser.current_url
        print(current_url)
        assert 'space/edit' in current_url, f"current_url doesn't content 'space/edit'"

    with allure.step('Делаем скриншот'):
        allure.attach(browser.get_screenshot_as_png(), name=r'C:\Users\DELL\PycharmProjects\AntHill\results',
                      attachment_type=AttachmentType.PNG), "Скриншот не создан"

    # page.edit_button()
    # time.sleep(3)
    # browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_edit.png')

# Run test:
# pytest .\tests\test_wiki_creation.py --alluredir results
