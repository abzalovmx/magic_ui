import os
from pages.customer_login import CustomerLogin

# не смог разобраться с прокси, временное решение
for var in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
    os.environ.pop(var, None)

# 35-26


def test_incorrect_login(driver):
    login_page = CustomerLogin(driver)
    login_page.open_page()
    login_page.fill_login_form('user@gmail.com', 'password')
    login_page.check_error_alert_text_is(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )

def test_correct_login(driver):
    login_page = CustomerLogin(driver)
    login_page.open_page()
    login_page.fill_login_form('user', 'password')
    login_page.check_error_alert_text_is('sss')