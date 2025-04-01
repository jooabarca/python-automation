# import asyncio
# from playwright.async_api import async_playwright

# async def run(playwright):
#     browser = await playwright.firefox.launch(headless=False)  # Use Firefox instead of Chromium
#     context = await browser.new_context()
#     page = await context.new_page()
    
#     # Navigate to the URL
#     await page.goto("https://www.saucedemo.com/")
    
#     # Find where to type
#     await page.fill("#user-name", "performance_glitch_user")
#     await page.fill("#password", "secret_sauce")
    
#     # Find login button and click
#     await page.click("#login-button")
    
#     # Validate that the login was successful by checking if the products page is loaded
#     try:
#         shopping_header = await page.wait_for_selector(".title", timeout=10000)
#         if await shopping_header.inner_text() == "Products":
#             print("Login successful.")
#         else:
#             print("Login failed1")
#     except Exception as e:
#         print("Login failed2")
    
#     # Busca un producto (por ejemplo, "Sauce Labs Backpack") y verifica que aparece.
#     try:
#         all_products = await page.query_selector_all(".inventory_item_name")
#         product_found = False
#         for product in all_products:
#             if await product.inner_text() == "Sauce Labs Backpack":
#                 print("Product found.")
#                 product_found = True
#                 break 
#         if not product_found:
#             print("Product not found.")
#     except Exception as e:
#         print("Class does not exist")
    
#     # Agregar el producto al carrito y verificar que se haya agregado correctamente
#     try:
#         await page.click("#add-to-cart-sauce-labs-backpack")
#         print("Product added to cart.")
#     except Exception as e:
#         print("Add to cart button not found.")
    
#     # Verificar que el producto se haya agregado al carrito
#     try:
#         cart = await page.wait_for_selector(".shopping_cart_badge", timeout=10000)
#         if await cart.inner_text() == "1":
#             print("Product added to cart")
#         else:
#             print("Product not added to cart")
#     except Exception as e:
#         print("no cart")
    
#     # Cierra sesión de la aplicación.
#     try:
#         await page.click("#react-burger-menu-btn")
#         await asyncio.sleep(3)
#         await page.click("#logout_sidebar_link")
#         print("Logged out successfully.")
#     except Exception as e:
#         print("Logout button not found.")
    
#     await asyncio.sleep(5)
#     await browser.close()

# async def main():
#     async with async_playwright() as playwright:
#         await run(playwright)

# asyncio.run(main())