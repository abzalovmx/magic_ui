from selenium.webdriver.common.by import By


email_field_loc = (By.ID, 'email')
password_field_loc = (By.ID, 'pass')
error_locator = (
            By.CSS_SELECTOR,
            '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]'
        )
button_loc = (By.ID, 'send2')