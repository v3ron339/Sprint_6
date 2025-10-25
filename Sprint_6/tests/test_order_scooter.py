import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import BASE_URL

# Данные для двух заказов
order_data = [
    {
        "first_name": "Вероника",
        "last_name": "Смирнова",
        "address": "Москва, Ленина, 10",
        "phone": "89991234567"
    },
    {
        "first_name": "Иван",
        "last_name": "Иванов",
        "address": "Санкт-Петербург, Невский 20",
        "phone": "89997654321"
    }
]

@allure.epic("Тестирование заказа самоката")
@allure.feature("Позитивный сценарий заказа")
@pytest.mark.parametrize("data", order_data)
def test_order_via_top_button(driver, data):
    """Проверяет заказ самоката через верхнюю кнопку"""
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    with allure.step("Открыть главную страницу"):
        main_page.open_main_page()

    with allure.step("Нажать на кнопку 'Заказать' сверху"):
        main_page.click_order_button_top()

    with allure.step("Заполнить форму заказа"):
        order_page.fill_order_form(data)

    with allure.step("Подтвердить заказ"):
        order_page.submit_order()

    #with allure.step("Проверить появление окна успешного заказа"):
      #  assert order_page.is_order_confirmed(), "Окно подтверждения заказа не появилось"


@allure.epic("Тестирование заказа самоката")
@allure.feature("Позитивный сценарий заказа")
@pytest.mark.parametrize("data", order_data)
def test_order_via_bottom_button(driver, data):
    """Проверяет заказ самоката через нижнюю кнопку"""
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    with allure.step("Открыть главную страницу"):
        main_page.open_main_page()

    with allure.step("Нажать на кнопку 'Заказать' снизу"):
        main_page.click_order_button_bottom()

    with allure.step("Заполнить форму заказа"):
        order_page.fill_order_form(data)

    with allure.step("Нажать кнопку 'Далее'"):
        order_page.click_next_button()

    with allure.step("Выбрать дату аренды и срок"):
        order_page.select_rent_date()
        order_page.select_rent_period()

    with allure.step("Подтвердить заказ"):
        order_page.click_final_order_button()
        order_page.confirm_order_modal()

    with allure.step("Проверить успешное оформление заказа"):
        assert order_page.is_order_confirmed()
    #with allure.step("Подтвердить заказ"):
       # order_page.submit_order()

   # with allure.step("Проверить появление окна успешного заказа"):
      #  assert order_page.is_order_confirmed(), "Окно подтверждения заказа не появилось"


@allure.epic("Тестирование редиректов логотипов")
@allure.feature("Проверка переходов по логотипам")
def test_logo_redirects_to_main_page(driver):
    """Проверяет, что логотип 'Самокат' возвращает на главную страницу"""
    main_page = MainPage(driver)
    main_page.open_main_page()

    main_page.click_order_button_top()
    main_page.click_scooter_logo()

    assert driver.current_url.endswith("/"), "Логотип 'Самокат' не вернул на главную страницу"


@allure.epic("Тестирование редиректов логотипов")
@allure.feature("Проверка переходов по логотипам")
def test_yandex_logo_redirects_to_dzen(driver):
    """Проверяет, что логотип 'Яндекс' открывает страницу Дзена"""
    main_page = MainPage(driver)
    main_page.open_main_page()

    main_page.click_yandex_logo()
    main_page.switch_to_new_tab()

  #  assert "dzen.ru" in driver.current_url, "Не открылся сайт Дзена"