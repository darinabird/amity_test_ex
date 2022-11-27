import time
import allure
from common.const import Configs
from pages.login_page import LoginHelper
from pages.directory_tab_page import DirectoryTab

cfg = Configs()


@allure.title('Test case 1')
def test_case_one(browser):
    lh = LoginHelper(browser)
    dr = DirectoryTab(browser)

    with allure.step('Go to auth page'):
        lh.go_to_page(lh.url_auth)
    with allure.step('Do login'):
        lh.do_login_by_admin()
    with allure.step('Go to directory tab'):
        dr.go_to_directory()
        time.sleep(2)
    with allure.step('Input employee name'):
        dr.input_employee_name()
        time.sleep(2)
    with allure.step('Click on location dropdown'):
        dr.select_location()
        time.sleep(2)
    with allure.step('Select USA location'):
        dr.select_usa_location()
        time.sleep(2)
    with allure.step('Click search'):
        dr.click_search()
        time.sleep(2)
    with allure.step('Check user contains "ch" in the name'):
        dr.find_and_display_names_with_ch()
        time.sleep(2)
    with allure.step('Do logout'):
        lh.do_logout()
