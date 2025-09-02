import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.home_page import HomePage


class OrderPage(HomePage):
    order_button = lambda _, cls_name: [By.XPATH, f'.//div[contains(@class, "{cls_name}")]/button[text()="Заказать"]']
    fields = lambda _, name: [By.CSS_SELECTOR, f'input[placeholder*="{name}"]']
    field_item = lambda _, name, text: [By.XPATH, f'.//input[contains(@placeholder, "{name}")]/following::button/div[text()="{text}"]']
    named_button = lambda _, name: [By.XPATH, f'.//button[text()="{name}"]']
    dropdown_field = [By.CLASS_NAME, 'Dropdown-placeholder']
    dropdown_item = lambda _, text: [By.XPATH, f'.//div[@class="Dropdown-option" and text()="{text}"]']
    checkbox = lambda _, name: [By.CSS_SELECTOR, f'label[for="{name}"]']
    middle_order_button = [By.XPATH, './/button[contains(@class, "Button_Middle") and text()="Заказать"]']
    modal_success = [By.XPATH, './/div[contains(@class, "Order_ModalHeader") and text()="Заказ оформлен"]']
    scooter_logo = [By.CSS_SELECTOR, f'a[class*="Header_LogoScooter"]']
    yandex_logo = [By.CSS_SELECTOR, f'a[class*="Header_LogoYandex"]']

    @allure.step('Клик на кнопку Заказать с классом "{cls_name}"')
    def click_on_order_button(self, cls_name):
        locator = self.order_button(cls_name)
        self.click(locator)

    @allure.step('Ввод текста "{text}" в поле "{field}"')
    def type_text_in_field(self, field, text):
        locator = self.fields(field)
        self.send_keys(locator, text)
        self.send_keys(locator, Keys.ENTER)

    @allure.step('Клик на поле "{field}" и выбор "{item}"')
    def click_on_field_and_select_item(self, field, item):
        locator_field = self.fields(field)
        locator_item = self.field_item(field, item)
        self.click(locator_field)
        self.click(locator_item)

    @allure.step('Клик на кнопку "{name}"')
    def click_on_named_button(self, name):
        locator = self.named_button(name)
        self.click(locator)

    @allure.step('Выбор выпадающего элемента "{item}"')
    def click_on_field_and_select_dropdown_item(self, item):
        locator_drop_field = self.dropdown_field
        self.click(locator_drop_field)

        locator_drop_item = self.dropdown_item(item)
        self.click(locator_drop_item)

    @allure.step('Клик на чекбокс "{name}"')
    def click_on_checkbox(self, name):
        locator = self.checkbox(name)
        self.click(locator)

    @allure.step('Клик на среднюю кнопку "Заказать"')
    def click_on_middle_order_button(self):
        locator = self.middle_order_button
        self.click(locator)

    @allure.step('Видно модальное окно с текстом об успешном оформлении заказа')
    def see_modal_success(self):
        locator = self.modal_success
        self.wait_until_visible(locator)

    @allure.step('Клик на лого самоката')
    def click_scooter_logo(self):
        locator = self.scooter_logo
        self.click(locator)

    @allure.step('Клик на лого яндекс')
    def click_yandex_logo(self):
        locator = self.yandex_logo
        self.click(locator)
