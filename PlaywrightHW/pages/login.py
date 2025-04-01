class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.header = ".title"

    async def enter_credentials(self, username, password):
        await self.page.fill(self.username_input, username)
        await self.page.fill(self.password_input, password)

    async def click_login(self):
        await self.page.click(self.login_button)

    async def is_logged_in(self):
        try:
            return await self.page.inner_text(self.header) == "Products"
        except Exception as e:
            print(f"Login check failed: {type(e).__name__} - {e}")
            return False