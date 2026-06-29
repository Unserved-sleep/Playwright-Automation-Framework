from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_flow(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    inv = InventoryPage(page)

    inv.add_to_cart("Sauce Labs Bike Light")
    inv.add_to_cart("Sauce Labs Bolt T-Shirt")
    inv.remove_from_cart("Sauce Labs Bike Light")
    inv.add_to_cart("Sauce Labs Fleece Jacket")
    inv.open_cart_page()

    # Cart Page Assertions
    cart_page = CartPage(page)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.finish_checkout()
    checkout_page.assert_checkout_complete()


    checkout_page.take_screenshot()