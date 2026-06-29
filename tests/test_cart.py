from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_product_cart_validation(page):
    # Setup - Navigate and Login
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Inventory Page Actions
    inventory_page = InventoryPage(page)
    
    # Add Backpack
    inventory_page.add_backpack_to_cart()
    
    # Add Bike Light
    inventory_page.add_bike_light_to_cart()

    # Verify cart badge count
    assert inventory_page.get_cart_badge_count() == "2"

    # Open Shopping Cart
    inventory_page.go_to_cart()

    # Cart Page Assertions
    cart_page = CartPage(page)
    
    # Verify both products exist
    item_names = cart_page.get_item_names()
    assert "Sauce Labs Backpack" in item_names
    assert "Sauce Labs Bike Light" in item_names
    
    # Assert total number of products
    assert cart_page.get_cart_items_count() == 2
