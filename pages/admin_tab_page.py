import time

from common.maintanance import BaseMethods
from common.locators import AdminTabLocators


class AdminTab(BaseMethods, AdminTabLocators):
    def go_to_admin_tab(self):
        self.find_and_wait_element(self.admin_tab).click()

    def click_job_dropdown(self):
        self.find_and_wait_element(self.job_dropdown).click()

    def choose_paygrades(self):
        self.find_and_wait_element(self.paygrades_option).click()

    def click_add_btn(self):
        self.find_and_wait_element(self.add_btn).click()

    def input_grade8_in_name_field(self):
        self.find_and_wait_element(self.name_field).click()
        self.find_and_wait_element(self.name_field).send_keys('Grade 8')

    def click_save(self):
        self.find_and_wait_element(self.submit_btn).click()

    def check_success_message_displayed(self):
        validation_message_got = self.find_and_wait_element(self.success_message).text
        result = self.is_element_present(self.success_message)
        validation_message_expected = "Success"
        print(f'\nValidation message: {validation_message_got}')
        assert result == True, f'Expected message: {validation_message_expected}\n' \
                               f'Got instead: {validation_message_got}'

    def click_add_assigned_currencies(self):
        self.find_and_wait_element(self.add_currencies_btn).click()

    def select_rupees(self):
        self.find_and_wait_element(self.currency_dropdown).click()
        self.find_and_wait_element(self.indian_rupees_option).click()

    def set_min_salary(self):
        self.find_and_wait_element(self.min_salary_field).click()
        self.find_and_wait_element(self.min_salary_field).send_keys('30000')

    def set_max_salary(self):
        self.find_and_wait_element(self.max_salary_field).click()
        self.find_and_wait_element(self.max_salary_field).send_keys('100000')

    def save_currency_btn(self):
        self.find_and_wait_element(self.submit_currency_btn).click()

    def check_currency_name(self):
        result = self.find_and_wait_element(self.currency_name_in_table).text
        expected = "Indian Rupee"
        assert result == expected, f'Expected currency: {expected}\nCurrent result: {result}'

    def check_salary(self):
        result_min = self.find_and_wait_element(self.min_salary_in_table).text
        result_max = self.find_and_wait_element(self.max_salary_in_table).text
        expected_min = '30000.00'
        expected_max = '100000.00'
        assert result_min == expected_min, f'Expected minimum salary: {expected_min}\nResult: {result_min}' \
                                           f'\n\nExpected maximun salary: {expected_max}\nResult: {result_max}'

    def delete_grade_8(self):
        warning = self.is_element_present(self.already_exists)
        if warning is True:
            self.click_job_dropdown()
            self.choose_paygrades()
            self.find_and_wait_element(self.delete_grade_8_btn).click()
            self.find_and_wait_element(self.confirm_deletion).click()
            self.click_add_btn()
            self.input_grade8_in_name_field()
        else:
            pass
