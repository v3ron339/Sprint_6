import allure
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Loc
class OrderPage(BasePage):
    """Page Object для страницы заказа самоката"""

    @allure.step("Заполнить данные пользователя")
    def fill_order_form(self, data):
        self.wait_for_visible(Loc.FIRST_NAME_INPUT).send_keys(data["first_name"])
        self.input_text(Loc.LAST_NAME_INPUT, data["last_name"])
        self.input_text(Loc.ADDRESS_INPUT, data["address"])
        self.click_element(Loc.METRO_STATION_FIELD)
        self.click_element(Loc.METRO_FIRST_OPTION)
        self.input_text(Loc.PHONE_INPUT, data["phone"])
        self.click_element(Loc.COOKIE_BANNER_BUTTON)

    # @allure.step("Закрыть cookie-баннер, если он присутствует")
     #def close_cookie_banner_if_present(self):
     #   """Нажимает 'да все привыкли', если баннер присутствует."""
       # try:
      #      button = self.click_element(Loc.COOKIE_BANNER_BUTTON)
      #      button.click()
      #      allure.attach(self.driver.get_screenshot_as_png(),
      #                    name="cookie_closed",
       #                   attachment_type=allure.attachment_type.PNG)
       # except TimeoutException:
       #     pass  # баннера нет — продолжаем те

   # @allure.step("Выбрать станцию метро")
    #def select_metro(self):
       # self.click_element(Loc.METRO_STATION_FIELD)
      #  self.click_element(Loc.METRO_FIRST_OPTION)

    @allure.step("Перейти к следующему шагу оформления")
    def submit_order(self):
        self.click_element(Loc.NEXT_BUTTON)
        self.click_element(Loc.RENT_DATE_FIELD)
        self.click_element(Loc.RENT_DATE_TODAY)
        self.click_element(Loc.RENT_PERIOD_DROPDOWN)
        self.click_element(Loc.RENT_PERIOD_DAY)
        self.click_element(Loc.COLOR_BLACK_CHECKBOX)
        self.click_element(Loc.ORDER_CONFIRM_BUTTON)
        self.click_element(Loc.ORDER_BUTTON_BOTTOM)
        self.click_element(Loc.YES_BUTTON)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_element(Loc.NEXT_BUTTON)
        
        # Задержка на случай анимации перехода
        sleep(1)

   # @allure.step("Заполнить данные аренды самоката")
   # def fill_rent_info(self):
   #     self.click_element(Loc.DATE_FIELD)
   #     self.click_element(Loc.RENT_DATE_TODAY)
   #     self.click_element(Loc.RENT_DROPDOWN)
   #     self.click_element(Loc.RENT_PERIOD_DROPDOWN)
   #     self.click_element(Loc.COLOR_BLACK)

    @allure.step("Подтвердить заказ")
    def is_order_confirmed(self):
        try:
            self.scroll_to_bottom()
            order_button = self.wait.until(EC.element_to_be_clickable(Loc.ORDER_BUTTON_FINAL))
            order_button.click()

            yes_button = self.wait.until(EC.element_to_be_clickable(Loc.YES_BUTTON))
            yes_button.click()

            self.wait_for_visible(Loc.ORDER_SUCCESS_POPUP)
            self.attach_screenshot("success_order_modal")

        except TimeoutException:
            self.attach_screenshot("order_confirmation_failed")
            raise AssertionError("Не удалось подтвердить заказ — элемент не найден или не кликабелен")


    @allure.step("Полный процесс оформления заказа")
    def complete_order(self, data):
        self.fill_customer_info(data)
        self.select_metro()
        self.go_next()
        self.fill_rent_info()
        self.confirm_order()