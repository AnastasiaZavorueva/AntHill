from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "input-56")
    LOGIN_PASS = (By.ID, "input-58")
    LOGIN_BTN = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div[4]/form/div/div[2]/button')