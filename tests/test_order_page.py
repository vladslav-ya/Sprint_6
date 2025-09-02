import allure
import pytest

from data import FIELD_DATA
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяется весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('data', FIELD_DATA)
    def test_positive_order_first_button(self, data, driver):
        order_page = OrderPage(driver)
        order_page.open_home_page()

        order_page.click_on_order_button(data[0])
        for field, text in data[1:5]:
            order_page.type_text_in_field(field, text)
        order_page.click_on_field_and_select_item(data[5], data[6])

        order_page.click_on_named_button('Далее')
        for field, text in data[7:9]:
            order_page.type_text_in_field(field, text)
        order_page.click_on_field_and_select_dropdown_item(data[9])
        order_page.click_on_checkbox(data[10])

        order_page.click_on_middle_order_button()
        order_page.click_on_named_button('Да')

        order_page.see_modal_success()
        order_page.click_on_named_button('Посмотреть статус')

        order_page.click_scooter_logo()
        order_page.wait_until_page_loaded()
        assert order_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/"

        order_page.click_yandex_logo()
        order_page.switch_to_new_page()
        assert "dzen.ru" in order_page.get_current_url()
