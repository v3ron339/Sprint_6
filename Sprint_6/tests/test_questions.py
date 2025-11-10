import pytest
from pages.main_page import MainPage

@pytest.mark.parametrize("index", list(range(8)))
def test_each_question_opens_answer(driver, index):
    home = MainPage(driver)
    home.open_home()
    home.close_cookie_banner()
    home.click_question_by_index(index)
    answer_text = home.get_answer_text_by_index(index)
    assert answer_text.strip() != ""