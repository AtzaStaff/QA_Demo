import time
import os
import logging

from dotenv import load_dotenv
from behave import *
from selenium.webdriver.support.wait import WebDriverWait

from functions.common_commands import globals

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
logging.basicConfig(level=logging.INFO)

@given(u'Open StaffWizard')
def step_impl(context):
    global driver, glb
    service = Service(executable_path = GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service = service)
    glb = globals(context.driver)
    glb.openBrowser(os.getenv('INSTANCE'), os.getenv('SERVER'))


@then(u'Login')
def step_impl(context):
    glb.text_type(5, 'id', 'name', os.getenv('USER'))
    glb.text_type(5, 'id', 'password', os.getenv('PASS'))
    glb.click_type(5, 'id', 'submit')


@given(u'Navigate across the panel until Add new employee forms')
def step_impl(context):
    glb.click_type( 5, "xpath", "//span[text()='Employees']")
    glb.click_type( 5, "xpath", "//span[contains(text(),'Available Employees')]")
    glb.click_type( 5, "xpath", "//a[contains(.,'Add New')]")


@then(u'Validate that the Unique ID field is not empty')
def step_impl(context):
    uniqueID = glb.validate(5, 'id', 'unique_id')
    if uniqueID:
        assert uniqueID, "The unique ID field is not emtpy"
    else:
        assert False, "the field is empty, but is a required field"


@then(u'Entering the First name')
def step_impl(context):
    glb.text_type(5, 'id', 'f_name', os.getenv('FIRST'))


@then(u'Entering the Middle name')
def step_impl(context):
    glb.text_type(5, 'id', 'm_name', os.getenv('MIDDLE'))


@then(u'Entering the Last name')
def step_impl(context):
    glb.text_type(5, 'id', 'l_name', os.getenv('LAST'))


@then(u'Select the country')
def step_impl(context):
    glb.select_type(5, 'xpath', f'//option[text() = "{os.getenv('COUNTRY')}"]', 'id', 'country', os.getenv('COUNTRY'))

@then(u'Entering the address')
def step_impl(context):
    address = os.getenv('STREET') + ' ' + os.getenv('CITY') + ', ' + os.getenv('ZIP')
    glb.text_type(5, 'id', 'searchTextField', str(address))
    glb.click_type(5, 'css selector', '.pac-item:nth-child(1)')


@then(u'Entering the PO Box')
def step_impl(context):
    glb.text_type(5, 'id', 'po-number', os.getenv('PO'))


@then(u'Entering the second address')
def step_impl(context):
    glb.text_type(5, 'id', 'address2', os.getenv('ADD2'))


@then(u'Validate that the State is the one enetered in Address field')
def step_impl(context):
    stateVal, state = glb.validate_select_type(5, 'id', 'state_field')
    if state.text == os.getenv('STATE'):
        assert True, f'The field has the correct option selected: {os.getenv('STATE')}'
    else:
        assert False, "The State field is empty, but is a required field"


@then(u'Validate that the City is the one enetered in Address field')
def step_impl(context):
    city = glb.validate_text_type(5, 'id', 'city_field')
    if city == os.getenv('CITY'):
        assert True, "The City field is not emtpy"
    else:
        assert False, "The City field is empty, but is a required field"


@then(u'Validate that the Zip Code is the one enetered in Address field')
def step_impl(context):
    zip = glb.validate_text_type(5, 'id', 'zip')
    if zip == os.getenv('ZIP'):
        assert True, "The Zip Code field is not emtpy"
    else:
        assert False, "The Zip Code field is empty, but is a required field"

@then(u'Entering the Mobile Phone')
def step_impl(context):
    glb.text_type(5, 'id', 'phone_format', os.getenv('PHONE'))


@then(u'Entering the Personal Email')
def step_impl(context):
    glb.text_type(5, 'id', 'p_email', os.getenv('EMAIL'))


@then(u'Entering the Date of Birth')
def step_impl(context):
    glb.text_type(5, 'id', 'dob', os.getenv('DOB'))


@then(u'Selecting the Race and Ethnicity')
def step_impl(context):
    glb.select_type(5,'xpath', f'//option[text() = "{os.getenv('RACE')}"]', 'name', 'ethnicity', os.getenv('RACE'))


@then(u'Entering the Social Secutiry Number')
def step_impl(context):
    ssn = glb.text_type(5, 'name', 'social_security', os.getenv('SSN'))


@then(u'Selecting the Region')
def step_impl(context):
    glb.select_type(5, 'xpath', f'//option[text() = "{os.getenv('REGION')}"]', 'id', 'master_region_id', os.getenv('REGION'))

@then(u'Selecting the Branch')
def step_impl(context):
    branch = glb.select_type(5, 'xpath', f'(//option[text() = "{os.getenv('BRANCH')}"])[3]', 'id', 'branch', os.getenv('BRANCH'))


@then(u'Selecting the Pay Type')
def step_impl(context):
    payType = glb.select_type(5, 'xpath', f'//option[text() = "{os.getenv('PAY_TYPE')}"]', 'id', 'pay_type', os.getenv('PAY_TYPE'))
    logging.info(payType)
    logging.info(os.getenv('PAY_TYPE'))

@then(u'Selecting the Employee Status')
def step_impl(context):
    glb.select_type(5, 'xpath', f'//option[text() = "{os.getenv('EMP_STATUS')}"]', 'id', 'status', os.getenv('EMP_STATUS'))


@then(u'Entering the Hire Date')
def step_impl(context):
    hire = glb.text_type(5, 'name', 'hire_date', os.getenv('HIRE'))
    hire.send_keys(Keys.ENTER)


@then(u'Entering the Join Date')
def step_impl(context):
    glb.text_type(5, 'name', 'joining_date', os.getenv('JOIN'))


@then(u'Click on the "Add Employee" button')
def step_impl(context):
    glb.click_type(5, 'name', 'submit1')
    time.sleep(2)


@then(u'Validate the successful addition')
def step_impl(context):
    add = glb.validate(5, 'xpath', f'//a[text()=("{os.getenv('FIRST')}")]')
    logging.info(add.text)
    if add.text == os.getenv('FIRST'):
        assert True, f"The employee {os.getenv('FIRST')} was added successfully"
    else:
        assert False, f"The employee {os.getenv('FISRT')} wasn't found, the addition falied"

    time.sleep(2)
    context.driver.close()



