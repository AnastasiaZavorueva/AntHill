import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.data import WikiPageData
from pages.wiki_creation_page import WikiCreationPage


def test_wiki_creation(browser, go_to_login):
    link = WikiPageData.WIKI_PAGE_URL
    page = WikiCreationPage(browser, link)
    page.open()
    page.click_create_button()
    # time.sleep(3)
    browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_login.png')
    page.choose_logo()
    # time.sleep(3)
    browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_logo.png')
    page.enter_title()
    # time.sleep(3)
    browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_title.png')
    page.enter_description()
    # time.sleep(3)
    browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_description.png')
    page.enter_category()
    # time.sleep(3)
    browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_category.png')
    page.add_button()
    # time.sleep(3)
    browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_add.png')
    page.edit_button()
    time.sleep(3)
    browser.save_screenshot(r'C:\Users\DELL\PycharmProjects\AntHill\results\result_edit.png')