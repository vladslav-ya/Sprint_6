import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class OrderPage:
    order_button = lambda _, cls_name: [By.XPATH, f'.//div[contains(@class, "{cls_name}")]/button[text()="Заказать"]']
    fields = lambda _, name: [By.CSS_SELECTOR, f'input[placeholder*="{name}"]']
    field_item = lambda _, text: [By.XPATH, f'.//button/div[text()="{text}"]']
    named_button = lambda _, name: [By.XPATH, f'.//button[text()="{name}"]']
    dropdown_field = [By.CLASS_NAME, 'Dropdown-placeholder']
    dropdown_item = lambda _, text: [By.XPATH, f'.//div[@class="Dropdown-option" and text()="{text}"]']
    checkbox = lambda _, name: [By.CSS_SELECTOR, f'label[for="{name}"]']
    middle_order_button = [By.XPATH, './/button[contains(@class, "Button_Middle") and text()="Заказать"]']
    modal_success = [By.XPATH, './/div[contains(@class, "Order_ModalHeader") and text()="Заказ оформлен"]']
    scooter_logo = [By.CSS_SELECTOR, f'a[class*="Header_LogoScooter"]']
    yandex_logo = [By.CSS_SELECTOR, f'a[class*="Header_LogoYandex"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик на кнопку Заказать с классом "{cls_name}"')
    def click_on_order_button(self, cls_name):
        element = self.driver.find_element(*self.order_button(cls_name))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Ввод текста "{text}" в поле "{field}"')
    def type_text_in_field(self, field, text):
        element = self.driver.find_element(*self.fields(field))
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of(element))
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    @allure.step('Клик на поле "{field}" и выбор "{item}"')
    def click_on_field_and_select_item(self, field, item):
        element = self.driver.find_element(*self.fields(field))
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of(element))
        element.click()

        self.driver.find_element(*self.field_item(item)).click()

    @allure.step('Клик на кнопку "{name}"')
    def click_on_named_button(self, name):
        element = self.driver.find_element(*self.named_button(name))
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Выбор выпадающего элемента "{item}"')
    def click_on_field_and_select_dropdown_item(self, item):
        element = self.driver.find_element(*self.dropdown_field)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of(element))
        element.click()

        item_elem = self.driver.find_element(*self.dropdown_item(item))
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(item_elem))
        item_elem.click()

    @allure.step('Клик на чекбокс "{name}"')
    def click_on_checkbox(self, name):
        element = self.driver.find_element(*self.checkbox(name))
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Клик на среднюю кнопку "Заказать"')
    def click_on_middle_order_button(self):
        element = self.driver.find_element(*self.middle_order_button)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Видно модальное окно с текстом об успешном оформлении заказа')
    def see_modal_success(self):
        element = self.driver.find_element(*self.modal_success)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of(element))

    @allure.step('Клик на лого самоката')
    def click_scooter_logo(self):
        element = self.driver.find_element(*self.scooter_logo)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of(element))
        element.click()

    @allure.step('Клик на лого яндекс')
    def click_yandex_logo(self):
        element = self.driver.find_element(*self.yandex_logo)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of(element))
        element.click()

    @allure.step('Ожидание загрузки страницы')
    def wait_until_page_loaded(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
