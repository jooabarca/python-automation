
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_names = (By.CLASS_NAME, "inventory_item_name")
        self.add_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        
    def find_product(self, product_name):
        products = self.driver.find_elements(*self.product_names)
        return any(product.text == product_name for product in products)
    
    def add_product_to_cart(self):
        self.driver.find_element(*self.add_cart_button).click()
    
    def is_product_in_cart(self):
        try:
            return self.driver.find_element(*self.cart_badge).text == "1"
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