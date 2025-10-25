import pytest
import allure
from pages.main_page import MainPage
from data.urls import BASE_URL
from data.faq_data import faq_questions


@allure.epic("Тестирование раздела FAQ")
@allure.feature("Раскрытие вопросов в разделе 'Вопросы о важном'")
@pytest.mark.parametrize("question_text, expected_answer", faq_questions)
def test_faq_expands_correct_answer(driver, question_text, expected_answer):
    """
    Проверяет, что при нажатии на вопрос FAQ открывается правильный ответ.
    """
    page = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        page.open_main_page()

    with allure.step("Прокрутить до раздела FAQ"):
        page.scroll_to_faq_section()

    with allure.step(f"Нажать на вопрос: {question_text}"):
        page.click_faq_question(question_text)

    with allure.step("Проверить текст ответа"):
        answer_text = page.get_faq_answer_text(question_text)
        assert expected_answer in answer_text, f"Ожидалось: {expected_answer}, получено: {answer_text}"