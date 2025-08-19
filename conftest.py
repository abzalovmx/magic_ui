import pytest
from selenium import webdriver
from time import sleep




@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    sleep(3)
    yield driver