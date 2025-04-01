class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.product_names = ".inventory_item_name"
        self.add_cart_button = "#add-to-cart-sauce-labs-backpack"
        self.cart_badge = ".shopping_cart_badge"

    async def find_product(self, product_name):
        elements = await self.page.query_selector_all(self.product_names)
        for element in elements:
            if await element.inner_text() == product_name:
                return True
        return False

    async def add_product_to_cart(self):
        await self.page.click(self.add_cart_button)

    async def is_product_in_cart(self):
        try:
            return await self.page.inner_text(self.cart_badge) == "1"
        except Exception as e:
            print(f"Cart check failed: {type(e).__name__} - {e}")
            return False