import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Loc


class OrderPage(BasePage):

    @allure.step("Заполнить данные клиента: {name} {surname}, адрес {address}, метро {metro}, телефон {phone}")
    def fill_order_form(self, name, surname, address, metro, phone):
        self.type(Loc.NAME_INPUT, name)
        self.type(Loc.SURNAME_INPUT, surname)
        self.type(Loc.ADDRESS_INPUT, address)

        # Выбор станции метро
        metro_input = self.find_element(Loc.METRO_INPUT)
        metro_input.send_keys(metro)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

        self.type(Loc.PHONE_INPUT, phone)
        self.click(Loc.NEXT_BUTTON)

        # Переход к форме аренды
        self.wait_for_visible(Loc.RENT_PERIOD_DROPDOWN)

    @allure.step("Заполнить форму аренды (цвет: чёрный)")
    def fill_rent_form_black(self, date, period, comment):
        self._fill_common_rent_fields(date, period)
        self.click(Loc.COLOR_BLACK)
        self.type(Loc.COMMENT, comment)

    @allure.step("Заполнить форму аренды (цвет: серый)")
    def fill_rent_form_grey(self, date, period, comment):
        self._fill_common_rent_fields(date, period)
        self.click(Loc.COLOR_GREY)
        self.type(Loc.COMMENT, comment)

    @allure.step("Заполнить форму аренды (произвольный цвет)")
    def fill_rent_form_custom(self, date, period, color_locator, comment):
        self._fill_common_rent_fields(date, period)
        self.click(color_locator)
        self.type(Loc.COMMENT, comment)

    def _fill_common_rent_fields(self, date, period):
        date_input = self.find_element(Loc.RENT_DATE)
        self.scroll_into_view_element(date_input)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located(Loc.DATEPICKER_POPUP)
        )

        dropdown = self.wait_for_clickable(Loc.RENT_PERIOD_DROPDOWN)
        self.scroll_into_view_element(dropdown)
        dropdown.click()

        # Выбор периода аренды напрямую по тексту
        option_locator = (Loc.RENT_OPTION_BY_TEXT[0], Loc.RENT_OPTION_BY_TEXT[1].format(period))
        self.click(option_locator)

    @allure.step("Подтвердить заказ")
    def submit_order(self):
        order_btn = self.wait_for_clickable(Loc.ORDER_SUBMIT_BUTTON)
        self.scroll_into_view_element(order_btn)
        self.safe_click(order_btn)

        confirm_btn = self.wait_for_clickable(Loc.ORDER_YES_BUTTON)
        self.scroll_into_view_element(confirm_btn)
        self.safe_click(confirm_btn)

    @allure.step("Проверить подтверждение заказа")
    def is_order_confirmed(self):
        self.wait_for_visible(Loc.ORDER_MODAL_TITLE)
        return True

   