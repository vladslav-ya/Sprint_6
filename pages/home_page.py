import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class HomePage:
    ques_section = [By.XPATH, '//div[text()="Вопросы о важном"]']
    ques_button = lambda _, text: [By.XPATH, f'.//div[@class="accordion__button" and text()="{text}"]']
    answer_und_question = [By.XPATH, './ancestor::div[@class="accordion__item"]/div[@class="accordion__panel"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание видимости раздела "Вопросы о важном"')
    def wait_visibility_question_about_important(self):
        element = self.driver.find_element(*self.ques_section)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of(element))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Клик на кнопку с вопросом "{question}"')
    def click_question(self, question):
        element = self.driver.find_element(*self.ques_button(question))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Получение ответа на вопрос "{question}"')
    def qet_answer_for_question(self, question):
        question_button = self.driver.find_element(*self.ques_button(question))
        element = question_button.find_element(*self.answer_und_question)
        return element.text
