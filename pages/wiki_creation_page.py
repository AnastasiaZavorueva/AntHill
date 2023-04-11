import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from pages.locators import WikiCreationPageLocators


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
        # add_button = self.browser.find_element(*WikiCreationPageLocators.ADD_BUTTON)
        # add_button.click()
        add_button2 = self.browser.find_element(*WikiCreationPageLocators.ADD_BUTTON2)
        add_button2.click()

    def edit_button(self):
        edit_button = self.browser.find_element(*WikiCreationPageLocators.EDIT_BUTTON)
        edit_button.submit()



    # def click_logo_icon(self):
    #     self.click_element(WikiCreationPageLocators.LOGO_ICON)
    #
    # def enter_title(self, title):
    #     self.enter_text(WikiCreationPageLocators.TITLE_FIELD, title)
    #
    # def enter_description(self, description):
    #     self.enter_text(WikiCreationPageLocators.DESCRIPTION_FIELD, description)
    #
    # def enter_category(self, category):
    #     self.enter_text(WikiCreationPageLocators.CATEGORY_FIELD, category)
    #
    # def click_add_button(self):
    #     self.click_element(WikiCreationPageLocators.ADD_BUTTON)
    #
    # def click_edit_button(self):
    #     self.click_element(WikiCreationPageLocators.EDIT_BUTTON)
    #
    # def click_section_list_button(self):
    #     self.click_element(WikiCreationPageLocators.SECTION_LIST_BUTTON)
    #
    # def create_wiki_space(self, title, description, category):
    #     self.click_create_button()
    #     self.click_logo_icon()
    #     self.enter_title(title)
    #     self.enter_description(description)
    #     self.enter_category(category)
    #     self.click_add_button()
    #     self.click_add_button()
    #     self.click_edit_button()
    #     self.click_section_list_button()
    #     self.wait_for_element_visibility(WikiCreationPageLocators.SUCCESS_MESSAGE)
