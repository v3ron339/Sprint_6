from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Loc


class OrderPage(BasePage):

    def fill_order_form(self, name, surname, address, metro, phone):
        self.type(Loc.NAME_INPUT, name)
        self.type(Loc.SURNAME_INPUT, surname)
        self.type(Loc. ADDRESS_INPUT, address)

        metro_input = self.find_element(Loc.METRO_INPUT)
        metro_input.clear()
        prefix = metro[:3]
        metro_input.send_keys(prefix)


        selected = False
        for _ in range(10):
            metro_input = self.find_element(Loc.METRO_INPUT)
            metro_input.send_keys(Keys.ARROW_DOWN)
            current = metro_input.get_attribute("value") or ""
            if current.strip().lower() == metro.strip().lower():
                metro_input.send_keys(Keys.ENTER)
                selected = True
                break

        if not selected:
            metro_input = self.find_element(Loc.METRO_INPUT)
            metro_input.send_keys(Keys.ENTER)
        

        self.type(Loc.PHONE_INPUT, phone)

        next_btn = self.find_element(Loc.NEXT_BUTTON)
        self.scroll_into_view_element(next_btn)
        try:
            self.click(Loc.NEXT_BUTTON)
        except Exception:
            self.js_click(next_btn)

        self.wait_for_visible(Loc.RENT_PERIOD_DROPDOWN)

    def fill_rent_form_black(self, date, period, comment):
        self._fill_common_rent_fields(date, period)
        self.click(Loc.COLOR_BLACK)
        self.type(Loc.COMMENT, comment)

    def fill_rent_form_grey(self, date, period, comment):
        self._fill_common_rent_fields(date, period)
        self.click(Loc.COLOR_GREY)
        self.type(Loc.COMMENT, comment)

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
            EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker"))
        )

        dropdown = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(Loc.RENT_DROPDOWN)
        )
        self.scroll_into_view_element(dropdown)
        try:
            dropdown.click()
        except:
            self.driver.execute_script("arguments[0].click();", dropdown)

        menu = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.Dropdown-menu[aria-expanded='true']"))
        )

        options = menu.find_elements(By.CSS_SELECTOR, "div.Dropdown-option")

        for opt in options:
            if opt.text.strip().lower() == period.strip().lower():
                self.scroll_into_view_element(opt)
                opt.click()
                break
        else:
            raise Exception(f"Не найдена опция срока аренды: {period}")

    def submit_order(self):
        order_btn = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(Loc.ORDER_SUBMIT_BUTTON)
        )
        self.scroll_into_view_element(order_btn)
        try:
            order_btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", order_btn)

        confirm_btn = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(Loc.ORDER_YES_BUTTON)
        )
        self.scroll_into_view_element(confirm_btn)
        try:
            confirm_btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", confirm_btn)

    def is_order_confirmed(self):
        self.wait_for_visible(Loc.ORDER_MODAL_TITLE)
        return True