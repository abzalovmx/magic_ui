from selenium.webdriver.common.by import By
from pages.base_page import BasePage


header_title_log = (By.XPATH, '//*[@id="header-title"]')

class SalePage(BasePage):
    page_url = '/sale.html'

    def check_page_header_is(self, text):
        header_title = self.find(header_title_log)
        assert header_title.text == text