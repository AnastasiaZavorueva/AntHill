from selenium.webdriver.common.keys import Keys

from locators.wiki_creation_page_locators import WikiCreationPageLocators
from pages.base_page import BasePage


class WikiCreationPage(BasePage):
    def click_create_button(self):
        create_btn = self.browser.find_element(*WikiCreationPageLocators.CREATE_BUTTON)
        create_btn.click()

    def choose_logo(self):
        logo_button = self.browser.find_element(*WikiCreationPageLocators.LOGO_BUTTON)
        logo_button.click()

        choose_logo = self.browser.find_element(*WikiCreationPageLocators.CHOOSE_LOGO)
        choose_logo.click()

    def enter_title(self):
        title_field = self.browser.find_element(*WikiCreationPageLocators.TITLE_FIELD)
        title_field.send_keys('Тестирование')

    def enter_description(self):
        description_field = self.browser.find_element(*WikiCreationPageLocators.DESCRIPTION_FIELD)
        description_field.send_keys('Тестирование проекта AntHill')

    def enter_category(self):
        category_field = self.browser.find_element(*WikiCreationPageLocators.CATEGORY_FIELD)
        category_field.send_keys('Тестирование')
        category_field.send_keys(Keys.ENTER)

    def add_button(self):
        add_button = self.browser.find_element(*WikiCreationPageLocators.ADD_BUTTON)
        add_button.click()

    def edit_button(self):
        edit_button = self.browser.find_element(*WikiCreationPageLocators.EDIT_BUTTON)
        edit_button.submit()

    def chapters_button(self):
        chapters_button = self.browser.find_element(*WikiCreationPageLocators.CHAPTERS_BUTTON)
        chapters_button.click()
