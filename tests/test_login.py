from pages.LoginPage import LoginPage

def test_login_valid(page):
    login_page = LoginPage(page)
    login_page.login()
    login_page.assert_login_success()