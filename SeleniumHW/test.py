import time
from selenium import webdriver
from pages.login import LoginPage
from pages.products import ProductsPage
from pages.menu import Menu

# Initialize WebDriver
driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/")

# Login
login_page = LoginPage(driver) 
login_page.enter_credentials("performance_glitch_user", "secret_sauce")
login_page.click_login()

# Validate login
time.sleep(2)
if login_page.is_logged_in():
    print("Login successful.")
else:
    print("Login failed.")

# Logout
menu = Menu(driver)
menu.logout()

# Close browser
time.sleep(5)
driver.quit()