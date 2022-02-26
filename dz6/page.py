from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.browser, self.browser.t) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, self.browser.t).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def click_link(self, link_text):
        self._click((By.LINK_TEXT, link_text))
        return self

    def click_by_locator(self, locator: tuple):
        self._click(locator)
    
    def click_by_elem(self, element):
        self._click_element(element)

    def check_element(self, locator: tuple):
        return self._element(locator)

    def input_item(self, text, locator: tuple):
        self._element(locator).send_keys(text)

    def wait_page(self, t: int):
        time.sleep(t)

class WebPage(BasePage):

    def __init__(self, browser, path=""):
        self.browser = browser
        self.browser.get(f'{self.browser.url}/{path}')

class AdminPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(f'{self.browser.url}/admin/')

    def login_with(self, user, pwd):
        self._element((By.CSS_SELECTOR, "#input-username")).send_keys(user)
        self._element((By.CSS_SELECTOR, "#input-password")).send_keys(pwd)
        self._element((By.CLASS_NAME, "btn")).click()
        
    def select_catalog(self):
        self._element((By.ID, "navigation"))
        self._element((By.ID, "menu-catalog")).click()

    def confirm_alert(self):
        try:
            WebDriverWait(self.browser, self.browser.t).until(EC.alert_is_present())
            self.browser.switch_to.alert.accept()
        except TimeoutException:
            raise AssertionError("Timed out waiting for show alert window")

    def select_products(self):
        self.select_catalog()
        self.click_link("Products")
        self.wait_page(1)
        header = self.check_element((By.CLASS_NAME, "page-header"))
        assert header.find_element(By.XPATH, "//h1").text == "Products"

    def check_success(self):
        success = self.check_element((By.CLASS_NAME, "alert"))
        assert "Success" in success.text

    def add_product(self):

        self.select_products()
        self.click_by_locator((By.CLASS_NAME, "btn-primary"))
        self.input_item("test_product", (By.CSS_SELECTOR, "#input-name1"))
        self.input_item("test", (By.CSS_SELECTOR, "#input-meta-title1"))
        self.click_link("Data")
        self.input_item("test_model", (By.CSS_SELECTOR, "#input-model"))
        self.click_by_locator((By.CLASS_NAME, "btn-primary"))
        self.check_success()

    def delete_prosuct(self):
        self.select_products()
        self.input_item("test_product", (By.CSS_SELECTOR, "#input-name"))
        self.click_by_locator((By.ID, "button-filter"))
        self.wait_page(1)
        form = self.check_element((By.ID, "form-product"))
        self.click_by_elem(form.find_elements(By.XPATH, "//input[@type='checkbox']")[1])
        self.click_by_locator((By.CLASS_NAME, "btn-danger"))
        self.confirm_alert()
        self.check_success()
