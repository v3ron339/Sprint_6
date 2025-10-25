import allure
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Loc
from data.urls import MAIN_PAGE_URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.driver.get(MAIN_PAGE_URL)

    @allure.step("Прокрутить до раздела FAQ")
    def scroll_to_faq_section(self):
        faq_block = self.wait_for_visible(Loc.FAQ_SECTION)
        self.scroll_to_element(faq_block)
        self.click_element(Loc.COOKIE_BANNER_BUTTON)

    @allure.step("Нажать на вопрос FAQ: {question_text}")
    def click_faq_question(self, question_text):
        questions = self.driver.find_elements(Loc.FAQ_QUESTION_BY_TEXT)
        for q in questions:
            if q.text.strip() == question_text.strip():
                self.scroll_to_element(q)
                q.click()
                return
        raise Exception(f"Вопрос с текстом '{question_text}' не найден")

    @allure.step("Получить текст ответа FAQ")
    def get_faq_answer_text(self, question_text):
        questions = self.driver.find_elements(Loc.FAQ_QUESTION_BY_TEXT)
        answers = self.driver.find_elements(Loc.FAQ_ANSWER_BY_TEXT)
        for q, a in zip(questions, answers):
            if q.text.strip() == question_text.strip():
                return a.text.strip()
        raise Exception(f"Ответ для вопроса '{question_text}' не найден")

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        button = self.wait_for_visible(Loc.ORDER_BUTTON_TOP)
        self.scroll_to_element(button)
        button.click()

    @allure.step("Прокрутить к нижней кнопке 'Заказать'")
    def scroll_to_bottom(self):
        button = self.wait_for_visible(Loc.ORDER_BUTTON_BOTTOM)
        self.scroll_to_element(button)

   # @allure.step("Нажать нижнюю кнопку 'Заказать'")
  #  def click_order_button_bottom(self):
   #     button = self.wait_for_visible(Loc.ORDER_BUTTON_BOTTOM)
  #      self.scroll_to_element(button)
  #      button.click()

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
      """Закрывает баннер (если есть), прокручивает и кликает по нижней кнопке 'Заказать'"""
      self.close_cookie_banner_if_present()

    # Прокрутка до кнопки
      button = self.wait_for_visible(Loc.ORDER_BUTTON_BOTTOM)
      self.scroll_to_element(button)

    # Иногда баннер появляется снова или задерживается — попробуем кликнуть безопасно
      try:
         button.click()
      except ElementClickInterceptedException:
         self.close_cookie_banner_if_present()  # ещё раз — на случай повторного появления
         self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
         self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        logo = self.wait_for_visible(Loc.SCOOTER_LOGO)
        logo.click()

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        logo = self.wait_for_visible(Loc.YANDEX_LOGO,)
        logo.click()

    @allure.step("Переключиться на новую вкладку (например, после клика по логотипу Яндекса)")
    def switch_to_new_tab(self):
        """Переключается на последнюю открытую вкладку браузера"""
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    @allure.step("Закрыть баннер с куками, если он присутствует")
    def close_cookie_banner_if_present(self):
        """Закрывает баннер с согласием на куки, если он отображается"""
        try:
            cookie_button = self.wait_for_visible(Loc.COOKIE_BANNER_BUTTON, timeout=5)
            cookie_button.click()
        except TimeoutException:
            pass  # баннера нет — продолжаем