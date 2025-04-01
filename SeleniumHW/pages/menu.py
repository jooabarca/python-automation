import time
from selenium.webdriver.common.by import By

class Menu:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")
    
    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        time.sleep(3)
        self.driver.find_element(*self.logout_button).click()

