from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize(
    "username,password,success",
    [
        ("standard_user", "secret_sauce", True),
        ("locked_out_user", "secret_sauce", False),
        ("problem_user", "secret_sauce", True),
    ]
)
def test_login_page(page, username, password, success):
    login_page = LoginPage(page)
    login_page.login(username, password)

    if success:
        login_page.assert_login_success()
    else:
        login_page.assert_login_error()