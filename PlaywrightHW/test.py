import asyncio
from playwright.async_api import async_playwright
from pages import LoginPage, ProductsPage, Menu

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.saucedemo.com/")

        login_page = LoginPage(page)
        await login_page.enter_credentials("performance_glitch_user", "secret_sauce")
        await login_page.click_login()

        if await login_page.is_logged_in():
            print("✅ Login successful.")
        else:
            print("❌ Login failed.")

        products_page = ProductsPage(page)
        if await products_page.find_product("Sauce Labs Backpack"):
            await products_page.add_product_to_cart()

        if await products_page.is_product_in_cart():
            print("✅ Product in cart.")

        menu = Menu(page)
        await menu.logout()

        await browser.close()

asyncio.run(run())