from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.complete_header = page.locator(".complete-header")
        self.complete_text = page.locator(".complete-text")

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def finish_checkout(self) -> None:
        self.finish_button.click()

    def assert_checkout_complete(self) -> None:
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
        expect(self.complete_header).to_have_text("Thank you for your order!")
        expect(self.complete_text).to_contain_text("Your order has been dispatched")

    def take_screenshot(self):
        self.page.screenshot(
            path="artifacts/screenshots/checkout_complete_page.png"
        )