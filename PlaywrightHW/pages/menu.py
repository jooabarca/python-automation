import asyncio

class Menu:
    def __init__(self, page):
        self.page = page
        self.menu_button = "#react-burger-menu-btn"
        self.logout_button = "#logout_sidebar_link"

    async def logout(self):
        await self.page.click(self.menu_button)
        await asyncio.sleep(2)
        await self.page.click(self.logout_button)