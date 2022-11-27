from common.maintanance import BaseMethods
from common.locators import DirectoryTabLocators


class DirectoryTab(BaseMethods, DirectoryTabLocators):
    def go_to_directory(self):
        self.find_and_wait_element(self.directory_tab).click()

    def input_employee_name(self):
        self.find_and_wait_element(self.employee_name).click()
        self.find_and_wait_element(self.employee_name).send_keys("ch")

    def select_location(self):
        self.find_and_wait_element(self.location).click()

    def find_and_display_names_with_ch(self):
        elements = self.find_and_wait_elements(self.name_out_of_search_locator)
        all_elements = [element.text for element in elements]
        name_list = list(all_elements)

        first_list = list(filter(lambda x: 'ch' in x, name_list))
        second_list = list(filter(lambda x: 'Ch' in x, name_list))
        result = first_list + second_list
        result_len = len(result)

        print(f'\n\nNames with "ch" and "Ch" are: {result}\nAmount of names: {result_len}\n')

    def select_usa_location(self):
        self.find_and_wait_element(self.location_usa).click()

    def click_search(self) -> None:
        self.find_and_wait_element(self.search).click()

    # def check_user_contains_ch(self) -> None:
    #     result = True
    #     current_result = self.is_element_present(self.ch_in_name)
    #     assert result == current_result
