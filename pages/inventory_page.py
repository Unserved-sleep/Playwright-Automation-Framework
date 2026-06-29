class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.shopping_cart_link = page.locator(".shopping_cart_link")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.backpack_add_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.bike_light_add_button = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def add_bike_light_to_cart(self):
        self.bike_light_add_button.click()

    def go_to_cart(self):
        self.shopping_cart_link.click()

    def get_cart_badge_count(self):
        return self.shopping_cart_badge.inner_text()
