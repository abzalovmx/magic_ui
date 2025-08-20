import pytest
from selenium import webdriver
from time import sleep




@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver