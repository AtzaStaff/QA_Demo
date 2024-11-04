import os
from dotenv import load_dotenv
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class globals():

    def __init__(self, driver):
        self.driver = driver

    def openBrowser(self, instance, server):
        url = 'http://' + str(instance) + '.' + str(server)
        self.driver.get(url)
        self.driver.maximize_window()

    def text_type(self, timeout, selector, key, value):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((selector, key))
            )
            element.send_keys(Keys.DELETE)
            element.send_keys(value)
            # element = WebDriverWait(self.driver, timeout).until(
            #     EC.visibility_of_element_located((selector, key))
            # )
            # if element.is_enabled() == True:
            #     element.clear()
            #     element.send_keys(value)
            # else:
            #     self.driver.close()
            return element
        except TimeoutException as ex:
            print(ex.msg)
            print("The element doesn't be found: " + selector + " -> " + key)

    def click_type(self, timeout, selector, key):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((selector, key))
            )
            element.click()
            return element
        except TimeoutException as ex:
            print(ex.msg)
            print("The element doesn't be found: " + selector + " -> " + key)

    def select_type(self, timeout, optSelector, optKey, selector, key, value):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((optSelector, optKey)))
            if element.is_enabled() == True:
                element = Select(self.driver.find_element(selector, key))
                element.select_by_visible_text(value)
        #     element = Select(WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((selector, key))))
        #     element.select_by_visible_text(value)
            return element
        except TimeoutException as ex:
            print(ex.msg)
            print("The element doesn't be found: " + selector + " -> " + key)


    def validate(self, timeout, selector, key):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((selector, key))
            )
            return element
        except TimeoutException as ex:
            print(ex.msg)
            print("The element doesn't be found: " + selector + " -> " + key)

    def validate_select_type(self, timeout, selector, key):
        load_dotenv()
        try:
            # element = WebDriverWait(self.driver, timeout).until(
            #     EC.presence_of_element_located((selector, key))
            # )
            # elementVal = element.get_attribute('value')
            # elementText = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(('xpath',f'(//option[@value="{os.getenv(value)}"])[1]')))
            # return elementVal, elementText
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located((selector, key)))
            elementVal = element.get_attribute('value')
            elementText = wait.until(EC.presence_of_element_located(('xpath', f'(//option[@value="{elementVal}"])[1]')))
            return elementVal, elementText
        except TimeoutException as ex:
            print(ex.msg)
            print("The element doesn't be found: " + selector + " -> " + key)

    def validate_text_type(self, timeout, selector, key):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((selector, key)))
            elementText = element.get_attribute('value')
            return elementText
        except TimeoutException as ex:
            print(ex.msg)
            print("The element doesn't be found: " + selector + " -> " + key)