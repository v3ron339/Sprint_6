import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1280,720")
    service = Service()
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()
    #-33-