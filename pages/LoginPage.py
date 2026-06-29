from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator('[data-test="error"]')

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_login_success(self) -> None:
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def assert_login_error(self, expected_message: str) -> None:
        expect(self.error_message).to_have_text(expected_message)