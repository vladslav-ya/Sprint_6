import allure
import pytest

from selenium import webdriver

from data import QUESTIONS_DATA
from pages.home_page import HomePage


class TestHomePage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка вопросов и ответов в разделе "Вопросы о важном"')
    @allure.description('Проверка соответствия вопроса и ответа')
    @pytest.mark.parametrize('question, check_answer', QUESTIONS_DATA)
    def test_questions_about_important(self, question, check_answer):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        home_page = HomePage(self.driver)

        home_page.wait_visibility_question_about_important()
        home_page.click_question(question)
        answer = home_page.qet_answer_for_question(question)
        assert answer == check_answer, 'Ответ не совпадает с тестовыми данными'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
