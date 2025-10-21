import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.order_page import OrderPage


@allure.title("Позитивный сценарий заказа самоката с разными данными и точками входа")
@pytest.mark.parametrize("order_button_locator", [
    HomePage.ORDER_BUTTON_TOP,
    HomePage.ORDER_BUTTON_BOTTOM
])
@pytest.mark.parametrize("name, surname, address, metro, phone, color", [
    ("Вероника", "Смирнова", "Москва, Лесная 12", "Лесная", "+79991112233", "black"),
    ("Анна", "Иванова", "Москва, Тверская 8", "Тверская", "+79995556677", "grey")
])
def test_successful_order_flow(driver, order_button_locator, name, surname, address, metro, phone, color):
    home = HomePage()
    order = OrderPage()
    wait = WebDriverWait(driver, 10)

    # --- 1. Переход к форме заказа --
    driver.find_element(*order_button_locator).click()

    # --- 2. Заполнение первой страницы --
    driver.find_element(*order.NAME_FIELD).send_keys(name)
    driver.find_element(*order.SURNAME_FIELD).send_keys(surname)
    driver.find_element(*order.ADDRESS_FIELD).send_keys(address)
    driver.find_element(*order.METRO_FIELD).send_keys(metro)
    driver.find_element(*order.PHONE_FIELD).send_keys(phone)
    driver.find_element(*order.NEXT_BUTTON).click()

    # --- 3. Заполнение второй страницы ---
    driver.find_element(*order.DATE_FIELD).send_keys("21.10.2025")
    driver.find_element(*order.RENTAL_PERIOD_DROPDOWN).click()
    driver.find_element(*order.RENTAL_PERIOD_OPTION).click()

    if color == "black":
        driver.find_element(*order.COLOR_BLACK).click()
    else:
        driver.find_element(*order.COLOR_GREY).click()

    driver.find_element(*order.COMMENT_FIELD).send_keys("Тестовый заказ")
    driver.find_element(*order.ORDER_SUBMIT_BUTTON).click()
    driver.find_element(*order.CONFIRM_YES_BUTTON).click()

    # --- 4. Проверка успешного оформления ---
    wait.until(EC.visibility_of_element_located(order.SUCCESS_MODAL))
    success_message = driver.find_element(*order.SUCCESS_MODAL).text
    assert "Заказ оформлен" in success_message, "Сообщение об успешном заказе не отображается"

@allure.title("Проверка перехода по логотипам Самокат и Яндекс")
def test_logos_navigation(driver):
    order = OrderPage()
    wait = WebDriverWait(driver, 10)

    # --- Нажать логотип Самоката ---
    driver.find_element(*order.SCOOTER_LOGO).click()
    wait.until(EC.url_contains("qa-scooter"))
    assert "qa-scooter.praktikum-services.ru" in driver.current_url, "Логотип Самоката не ведёт на главную"

    # --- Нажать логотип Яндекса ---
    yandex_logo = driver.find_element(*order.YANDEX_LOGO)
    yandex_logo.click()

    # Переключиться в новое окно
    driver.switch_to.window(driver.window_handles[1])
    assert "dzen.ru" in driver.current_url or "yandex.ru" in driver.current_url, \
        "Логотип Яндекса не открыл Дзен в новом окне"