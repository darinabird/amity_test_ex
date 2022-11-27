from selenium.webdriver.common.by import By


class LoginPageLocators:
    login_input = (By.CSS_SELECTOR, '[placeholder="Username"]')
    password_input = (By.CSS_SELECTOR, '[placeholder="Password"]')
    accept_btn = (By.CSS_SELECTOR, '[type="submit"]')
    profile_widget = (By.CSS_SELECTOR, '[alt="profile picture"]')
    logout_btn = (By.CSS_SELECTOR, 'a[href*="logout"]')


class DirectoryTabLocators:
    directory_tab = (By.CSS_SELECTOR, 'li.oxd-main-menu-item-wrapper:nth-child(9) > a:nth-child(1) > span:nth-child(2)')
    employee_name = (By.CSS_SELECTOR, '[placeholder="Type for hints..."]')
    location = (By.CSS_SELECTOR,
                'div > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > '
                'div')
    location_usa = (By.XPATH, '*//div[contains(@class, "oxd-select-option")]//span[contains(text(), "USA")]')
    ch_in_name = (
        By.XPATH, '//*[contains(@class, "sheet")][contains(p, "Ch") or contains(p, "ch")]')
    name_out_of_search_locator = (By.XPATH, '//p[@class="oxd-text oxd-text--p orangehrm-directory-card-header '
                                            '--break-words"]')
    search = (By.CSS_SELECTOR, '[type="submit"]')


class AdminTabLocators:
    admin_tab = (By.CSS_SELECTOR, 'a[href*="AdminModule"]')
    job_dropdown = (By.XPATH, '//span[contains(text(), "Job")]')
    paygrades_option = (By.CSS_SELECTOR, '.oxd-dropdown-menu > li:nth-child(2) > a:nth-child(1)')
    add_btn = (By.CSS_SELECTOR, '.oxd-button')
    name_field = (By.CSS_SELECTOR, 'input.oxd-input:nth-child(1)')
    submit_btn = (By.CSS_SELECTOR, 'button[type="submit"]')
    # success_message = (By.CSS_SELECTOR, '[aria-live="assertive"]')
    success_message = (By.CSS_SELECTOR, 'p.oxd-text--toast-message')
    add_currencies_btn = (By.CSS_SELECTOR, 'button.oxd-button--secondary:nth-child(2)')
    currency_dropdown = (By.CSS_SELECTOR, '.oxd-select-text-input')
    indian_rupees_option = (By.XPATH, '//span[contains(text(), "Indian")]')
    min_salary_field = (By.CSS_SELECTOR, 'div.oxd-form-row:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input')
    max_salary_field = (By.CSS_SELECTOR, 'div.oxd-grid-item:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
    submit_currency_btn = (By.CSS_SELECTOR, 'div.oxd-form-actions:nth-child(4) > button:nth-child(3)')
    currency_name_in_table = (By.CSS_SELECTOR, 'div.oxd-table-cell:nth-child(2) > div')
    min_salary_in_table = (By.CSS_SELECTOR, 'div.oxd-table-cell:nth-child(3) > div')
    max_salary_in_table = (By.CSS_SELECTOR, 'div.oxd-table-cell:nth-child(4) > div')

    already_exists = (By.CSS_SELECTOR, 'span.oxd-text:nth-child(3)')
    delete_grade_8_btn = (By.CSS_SELECTOR, 'div.oxd-table-card:nth-child(6) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)')
    confirm_deletion = (By.CSS_SELECTOR, 'button.oxd-button:nth-child(2)')

