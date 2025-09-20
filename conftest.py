import pytest
from selenium import webdriver
from time import sleep
from pages.sale_page import SalePage
from pages.customer_login import CustomerLogin


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver


@pytest.fixture
def sale_page(driver):
    return SalePage(driver)

@pytest.fixture
def customer_login(driver):
    return CustomerLogin(driver)