from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.header = (By.CLASS_NAME, "title")
    
    def enter_credentials(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def is_logged_in(self):
        try:
            return self.driver.find_element(*self.header).text == "Products"
        except NoSuchElementException:
            print("Element not found")
            return False
        except TimeoutException:
            print("Took too long")
            return False
        except ElementNotInteractableException:
            print("Can't interact with element")
            return False
        except StaleElementReferenceException:
            print("Stale element! Page changed after element was found.")
            return False