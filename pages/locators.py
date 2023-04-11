from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "input-56")
    LOGIN_PASS = (By.ID, "input-58")
    LOGIN_BTN = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div[4]/form/div/div[2]/button')


class WikiCreationPageLocators:
    CREATE_BUTTON = (By.XPATH, '//*[@id="app"]/div/div[2]/div/main/div/nav/div/div/button/span[3]')
    LOGO_BUTTON = (By.XPATH, '//*[@id="app"]/div/div[2]/div/main/div/main/div/form/div/div[1]/div/div[1]')
    CHOOSE_LOGO = (By.XPATH, '/html/body/div[2]/div[2]/div/div/button[1]')  # Выбираем любое лого
    TITLE_FIELD = (By.XPATH, '//*[@id="title"]')  # Вводим название
    DESCRIPTION_FIELD = (By.ID, 'description')  # Вводим описание
    CATEGORY_FIELD = (By.ID, 'category')  # Вводим категорию
    # ADD_BUTTON = (By.CSS_SELECTOR, 'css=.v-btn--elevated:nth-child(1) > .v-btn__content')
    ADD_BUTTON2 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/main/div/main/div/form/div/div[5]/button[2]')
    EDIT_BUTTON = (By.XPATH, 'xpath=//div[5]/button[2]/span[3]')
