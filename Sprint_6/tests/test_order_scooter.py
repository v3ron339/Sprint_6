import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import order_data_set_1, order_data_set_2


@allure.feature("Оформление заказа самоката")
@allure.story("Проверка полного сценария оформления заказа через разные точки входа")
class TestOrder:

    @allure.title("Полный сценарий заказа чёрного самоката (через хедер)")
    def test_order_black_header(self, driver):
        with allure.step("Открыть главную страницу"):
            home = MainPage(driver)
            home.open_home()
            home.close_cookie_banner()

        with allure.step("Нажать на верхнюю кнопку 'Заказать'"):
            home.click_order_button_header()

        with allure.step("Заполнить форму данных пользователя"):
            order_page = OrderPage(driver)
            order_page.fill_order_form(
                name=order_data_set_1["name"],
                surname=order_data_set_1["surname"],
                address=order_data_set_1["address"],
                metro=order_data_set_1["metro"],
                phone=order_data_set_1["phone"]
            )

        with allure.step("Заполнить форму аренды — чёрный самокат"):
            order_page.fill_rent_form_black(
                date=order_data_set_1["date"],
                period=order_data_set_1["period"],
                comment=order_data_set_1["comment"]
            )

        with allure.step("Подтвердить заказ"):
            order_page.submit_order()

        with allure.step("Проверить успешное оформление заказа"):
            assert order_page.is_order_confirmed(), "Заказ не был подтверждён"

    @allure.title("Полный сценарий заказа чёрного самоката (через футер)")
    def test_order_black_footer(self, driver):
        with allure.step("Открыть главную страницу"):
            home = MainPage(driver)
            home.open_home()
            home.close_cookie_banner()

        with allure.step("Нажать на нижнюю кнопку 'Заказать'"):
            home.click_order_button_footer()

        with allure.step("Заполнить форму данных пользователя"):
            order_page = OrderPage(driver)
            order_page.fill_order_form(
                name=order_data_set_1["name"],
                surname=order_data_set_1["surname"],
                address=order_data_set_1["address"],
                metro=order_data_set_1["metro"],
                phone=order_data_set_1["phone"]
            )

        with allure.step("Заполнить форму аренды — чёрный самокат"):
            order_page.fill_rent_form_black(
                date=order_data_set_1["date"],
                period=order_data_set_1["period"],
                comment=order_data_set_1["comment"]
            )

        with allure.step("Подтвердить заказ"):
            order_page.submit_order()

        with allure.step("Проверить успешное оформление заказа"):
            assert order_page.is_order_confirmed(), "Заказ не был подтверждён"

    @allure.title("Полный сценарий заказа серого самоката (через хедер)")
    def test_order_grey_header(self, driver):
        with allure.step("Открыть главную страницу"):
            home = MainPage(driver)
            home.open_home()
            home.close_cookie_banner()

        with allure.step("Нажать на верхнюю кнопку 'Заказать'"):
            home.click_order_button_header()

        with allure.step("Заполнить форму данных пользователя"):
            order_page = OrderPage(driver)
            order_page.fill_order_form(
                name=order_data_set_2["name"],
                surname=order_data_set_2["surname"],
                address=order_data_set_2["address"],
                metro=order_data_set_2["metro"],
                phone=order_data_set_2["phone"]
            )

        with allure.step("Заполнить форму аренды — серый самокат"):
            order_page.fill_rent_form_grey(
                date=order_data_set_2["date"],
                period=order_data_set_2["period"],
                comment=order_data_set_2["comment"]
            )

        with allure.step("Подтвердить заказ"):
            order_page.submit_order()

        with allure.step("Проверить успешное оформление заказа"):
            assert order_page.is_order_confirmed(), "Заказ не был подтверждён"

    @allure.title("Полный сценарий заказа серого самоката (через футер)")
    def test_order_grey_footer(self, driver):
        with allure.step("Открыть главную страницу"):
            home = MainPage(driver)
            home.open_home()
            home.close_cookie_banner()

        with allure.step("Нажать на нижнюю кнопку 'Заказать'"):
            home.click_order_button_footer()

        with allure.step("Заполнить форму данных пользователя"):
            order_page = OrderPage(driver)
            order_page.fill_order_form(
                name=order_data_set_2["name"],
                surname=order_data_set_2["surname"],
                address=order_data_set_2["address"],
                metro=order_data_set_2["metro"],
                phone=order_data_set_2["phone"]
            )

        with allure.step("Заполнить форму аренды — серый самокат"):
            order_page.fill_rent_form_grey(
                date=order_data_set_2["date"],
                period=order_data_set_2["period"],
                comment=order_data_set_2["comment"]
            )

        with allure.step("Подтвердить заказ"):
            order_page.submit_order()

        with allure.step("Проверить успешное оформление заказа"):
            assert order_page.is_order_confirmed(), "Заказ не был подтверждён"