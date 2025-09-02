from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def wait(self):
        return WebDriverWait(self.driver, 5)

    def wait_until_visible(self, locator: list):
        element = self.driver.find_element(*locator)
        self.wait.until(expected_conditions.visibility_of(element))

    def wait_until_clickable(self, locator: list):
        element = self.driver.find_element(*locator)
        self.wait.until(expected_conditions.element_to_be_clickable(element))

    def scroll_into_view(self, locator: list):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click(self, locator: list):
        element = self.driver.find_element(*locator)
        self.wait_until_clickable(locator)
        self.scroll_into_view(locator)
        element.click()

    def send_keys(self, locator: list, text):
        element = self.driver.find_element(*locator)
        self.wait_until_visible(locator)
        self.scroll_into_view(locator)
        element.send_keys(text)

    def get_text(self, locator: list) -> str:
        element = self.driver.find_element(*locator)
        self.wait_until_visible(locator)
        self.scroll_into_view(locator)
        return element.text

    def get_current_url(self) -> str:
        return self.driver.current_url

    def wait_until_page_loaded(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    def open_page(self, url: str):
        self.driver.get(url)
        self.wait_until_page_loaded()

    def switch_to_new_page(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_until_page_loaded()
