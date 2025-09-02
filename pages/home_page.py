import allure

from selenium.webdriver.common.by import By

from data import URLS
from pages.base_page import BasePage


class HomePage(BasePage):
    ques_section = [By.XPATH, '//div[text()="Вопросы о важном"]']
    ques_button = lambda _, text: [By.XPATH, f'.//div[@class="accordion__button" and text()="{text}"]']
    answer_und_question = lambda _, text: [By.XPATH, f'.//div[@class="accordion__button" and text()="{text}"]/ancestor::div[@class="accordion__item"]/div[@class="accordion__panel"]']

    @allure.step('Ожидание видимости раздела "Вопросы о важном"')
    def wait_visibility_question_about_important(self):
        locator = self.ques_section
        self.wait_until_visible(locator)
        self.scroll_into_view(locator)

    @allure.step('Клик на кнопку с вопросом "{question}"')
    def click_question(self, question):
        locator = self.ques_button(question)
        self.click(locator)

    @allure.step('Получение ответа на вопрос "{question}"')
    def qet_answer_for_question(self, question):
        locator = self.answer_und_question(question)
        return self.get_text(locator)

    @allure.step('Открыть домашнюю страницу')
    def open_home_page(self):
        self.open_page(URLS["home_page"])
