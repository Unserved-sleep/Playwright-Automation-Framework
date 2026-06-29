from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_product_cart_validation(page):
    # Setup - Navigate and Login
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
    
    # Verify both products exist
    item_names = cart_page.get_item_names()
    assert "Sauce Labs Bolt T-Shirt" in item_names
    assert "Sauce Labs Fleece Jacket" in item_names
    assert cart_page.get_cart_items_count() == 2

    cart_page.take_screenshot()
