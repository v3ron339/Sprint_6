import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    # -------------------------
    # Навигация
    # -------------------------
    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    # -------------------------
    # Поиск элементов
    # -------------------------
    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти все элементы: {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Ожидать, пока элемент станет видимым: {locator}")
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидать, пока элемент станет кликабельным: {locator}")
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # -------------------------
    # Взаимодействие
    # -------------------------
    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        element = self.wait_for_clickable(locator)
        self.scroll_into_view_element(element)
        try:
            element.click()
        except ElementClickInterceptedException:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="click_intercepted",
                          attachment_type=allure.attachment_type.PNG)
            self.js_click(element)

    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def type(self, locator, text):
        element = self.find_element(locator)
        self.scroll_into_view_element(element)
        element.clear()
        element.send_keys(text)

    # -------------------------
    # Скролл и JS
    # -------------------------
    @allure.step("Прокрутить страницу к элементу")
    def scroll_into_view_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Клик по элементу через JS")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Выполнить JavaScript-команду")
    def js_scroll(self, script):
        self.driver.execute_script(script)

    # -------------------------
    # Окна и переходы
    # -------------------------
    @allure.step("Ожидание открытия новой вкладки и переключение на неё")
    def wait_for_new_window_and_switch(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидание, пока URL перестанет быть пустым")
    def wait_for_url_not_blank(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url != "about:blank")