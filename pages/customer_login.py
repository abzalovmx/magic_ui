from selenium.webdriver.common.by import By
from pages.base_page import BasePage


email_field_loc = (By.ID, 'email')
password_field_loc = (By.ID, 'pass')
error_locator = (
            By.CSS_SELECTOR,
            '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]'
        )
button_loc = (By.ID, 'send2')


class CustomerLogin(BasePage):
    page_url = '/customer/account/login'

    def fill_login_form(self, login, password):
        email_field = self.find(email_field_loc)
        password_field = self.find(password_field_loc)
        button = self.find(button_loc)
        email_field.send_keys(login)
        password_field.send_keys(password)
        button.click()


    def check_error_alert_text_is(self, text):
        error_alert = self.driver.find_element(error_locator)
        assert error_alert.text == text