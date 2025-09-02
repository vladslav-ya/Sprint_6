import allure
import pytest

from data import QUESTIONS_DATA
from pages.home_page import HomePage


class TestHomePage:

    @allure.title('Проверка вопросов и ответов в разделе "Вопросы о важном"')
    @allure.description('Проверка соответствия вопроса и ответа')
    @pytest.mark.parametrize('question, check_answer', QUESTIONS_DATA)
    def test_questions_about_important(self, question, check_answer, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()

        home_page.wait_visibility_question_about_important()
        home_page.click_question(question)
        answer = home_page.qet_answer_for_question(question)
        assert answer == check_answer, 'Ответ не совпадает с тестовыми данными'
