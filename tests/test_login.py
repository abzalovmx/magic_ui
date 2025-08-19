from selenium.webdriver.common.by import By
import os


# не смог разобраться с прокси, временное решение
for var in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
    os.environ.pop(var, None)

# 35-26


def test_incorrect_login(driver):
    driver.get('https://magento.softwaretestingboard.com/customer/account/login')
    email_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')
    button = driver.find_element(By.ID, 'send2')
    email_field.send_keys('asdad@dasd.com')
    password_field.send_keys('asd')
    button.click()
    error_alert = driver.find_element(
        By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]'
    )
    assert  error_alert.text == (
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )