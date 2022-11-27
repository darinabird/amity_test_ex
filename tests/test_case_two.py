import time
import allure
from common.const import Configs
from pages.login_page import LoginHelper
from pages.admin_tab_page import AdminTab

cfg = Configs()


@allure.title('Test case 2')
def test_case_two(browser):
    lh = LoginHelper(browser)
    ad = AdminTab(browser)

    with allure.step('Go to auth page'):
        lh.go_to_page(lh.url_auth)
    with allure.step('Do login'):
        lh.do_login_by_admin()
    with allure.step('Go to admin tab'):
        ad.go_to_admin_tab()
        time.sleep(2)
    with allure.step('Choose pay grades'):
        ad.click_job_dropdown()
        time.sleep(2)
        ad.choose_paygrades()
        time.sleep(2)
    with allure.step('Click add button'):
        ad.click_add_btn()
        time.sleep(2)
    with allure.step('Input "Grade 8" in the name field'):
        ad.input_grade8_in_name_field()
        ad.delete_grade_8()
        time.sleep(2)
    with allure.step('Save'):
        ad.click_save()
    with allure.step('Verify success message is displayed'):
        ad.check_success_message_displayed()
    with allure.step('Click on add in assigned currencies'):
        ad.click_add_assigned_currencies()
        time.sleep(2)
    with allure.step('Set indian rupees'):
        ad.select_rupees()
        time.sleep(2)
    with allure.step('Set minimum salary'):
        ad.set_min_salary()
        time.sleep(2)
    with allure.step('Set maximum salary'):
        ad.set_max_salary()
        time.sleep(2)
    with allure.step('Save currency'):
        ad.save_currency_btn()
        time.sleep(2)
    with allure.step('Verify success message is displayed'):
        ad.check_success_message_displayed()
        time.sleep(4)
    with allure.step('Verify currency name input'):
        ad.check_currency_name()
        time.sleep(2)
    with allure.step('Verify salary input'):
        ad.check_salary()
        time.sleep(2)
