import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый класс Page Object.
    Содержит общие методы для всех страниц проекта.
    """

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # -------------------------
    # Методы поиска элементов
    # -------------------------
    @allure.step("Поиск элемента: {locator}")
    def find_element(self, locator):
        """Находит элемент на странице с ожиданием"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="element_not_found",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Элемент не найден: {locator}")

    @allure.step("Поиск всех элементов: {locator}")
    def find_elements(self, locator):
        """Возвращает список элементов (может быть пустым)"""
        return self.driver.find_elements(*locator)

    # -------------------------
    #  Методы взаимодействия
    # -------------------------
    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator):
        """Ожидает видимости и кликает по элементу"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def input_text(self, locator, text):
        """Очищает поле и вводит текст"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    # -------------------------
    # Методы прокрутки
    # -------------------------
    @allure.step("Прокрутка до элемента: {element}")
    def scroll_to_element(self, element):
        """Прокручивает страницу до элемента"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Прокрутка в самый низ страницы")
    def scroll_to_bottom(self):
        """Прокручивает страницу до конца"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # -------------------------
    #  Методы ожидания
    # -------------------------
    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_visible(self, locator, timeout=10):
        """Ожидает, пока элемент станет видимым"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание появления текста '{text}' в элементе: {locator}")
    def wait_for_text(self, locator, text, timeout=10):
        """Ожидает появления указанного текста"""
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    # -------------------------
    #  Скриншоты и проверки
    # -------------------------
    @allure.step("Прикрепить скриншот текущей страницы")
    def attach_screenshot(self, name="screenshot"):
        """Сохраняет скриншот для Allure"""
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=name,
                      attachment_type=allure.attachment_type.PNG)

    @allure.step("Проверка URL содержит: {expected}")
    def assert_url_contains(self, expected):
        """Проверяет, что текущий URL содержит подстроку"""
        current = self.driver.current_url
        assert expected in current, f"Ожидали, что URL содержит '{expected}', но текущий: '{current}'"