import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage


@allure.title("Тесты раздела 'Вопросы о важном'")
@pytest.mark.usefixtures("driver")
class TestFAQSection:

    @pytest.mark.parametrize("question, answer", [
        (HomePage.QUESTION_1, HomePage.ANSWER_1),
        (HomePage.QUESTION_2, HomePage.ANSWER_2),
        (HomePage.QUESTION_3, HomePage.ANSWER_3),
        (HomePage.QUESTION_4, HomePage.ANSWER_4),
        (HomePage.QUESTION_5, HomePage.ANSWER_5),
        (HomePage.QUESTION_6, HomePage.ANSWER_6),
        (HomePage.QUESTION_7, HomePage.ANSWER_7),
        (HomePage.QUESTION_8, HomePage.ANSWER_8),
    ])
    def test_faq_answer_visible_after_click(self, driver, question, answer):
        """Проверка: при нажатии на стрелку открывается текст ответа."""
        wait = WebDriverWait(driver, 5)

        # Прокрутить страницу вниз до раздела FAQ----
        faq_block = driver.find_element(*HomePage.FAQ_BLOCK)
        driver.execute_script("arguments[0].scrollIntoView();", faq_block)

        # Нажать на вопрос
        driver.find_element(*question).click()

        # Проверить, что текст стал видимым
        wait.until(EC.visibility_of_element_located(answer))
        is_visible = driver.find_element(*answer).is_displayed()

        assert is_visible, f"Ответ на вопрос {question} не открылся!"