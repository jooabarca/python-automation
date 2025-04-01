import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#Abre un driver y navega a https://www.saucedemo.com/
driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/")

#find where to type
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")

#type credentials
username_input.send_keys("performance_glitch_user")
password_input.send_keys("secret_sauce")

#find login button
login_button = driver.find_element(By.ID, "login-button")

#click button
login_button.click()

#Valida que el inicio de sesión fue exitoso comprobando que se carga la página de productos.
try:
    shopping_header = driver.find_element(By.CLASS_NAME, "title")
    if shopping_header.text == "Products":
        print("Login successful.")
    else:
        print("Login failed1")
except NoSuchElementException:
    print("Login failed2")

#Busca un producto (por ejemplo, "Sauce Labs Backpack") y verifica que aparece.
try:
    all_products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    for product in all_products:
        if product.text == "Sauce Labs Backpack":
            print("Product found.")
            break   
except NoSuchElementException:
    print("Class does not exist")

#Agregar el producto al carrito y verificar que se haya agregado correctamente
add_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_cart_button.click()

try:
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    if cart.text == "1":
        print("Product added to cart")
    else:
        print("Product not added to cart")
except NoSuchElementException:
    print("no cart")

#Cierra sesión de la aplicación.
menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
menu_button.click()
time.sleep(3)
logout_button = driver.find_element(By.ID, "logout_sidebar_link")
logout_button.click()



time.sleep(5)
driver.quit()