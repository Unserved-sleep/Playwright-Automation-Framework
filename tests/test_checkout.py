from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

def test_checkout_flow(page):
    login_page = LoginPage(page)
    login_page.login()
    login_page.assert_login_success()

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.finish_checkout()
    checkout_page.assert_checkout_complete()