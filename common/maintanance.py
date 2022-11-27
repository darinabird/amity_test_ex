from time import sleep
from common.const import Configs
from selenium.webdriver import WebKitGTK
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from common.locators import LoginPageLocators

cfg = Configs()
selenium_exceptions = (exceptions.WebDriverException, exceptions.TimeoutException, exceptions.NoSuchElementException)


class BaseMethods:
    def __init__(self, driver: WebKitGTK):
        self.driver = driver
        self.url_base_host = cfg.url_base_host
        self.url_auth = self.url_base_host + "/web/index.php/auth/login"

    def find_and_wait_element(self, locator, time=5):
        self.driver.implicitly_wait(time)
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"\nCan't find element by locator {locator}")

    def find_and_wait_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"\nCan't find elements by locator {locator}")

    def is_element_present(self, locator) -> bool:
        try:
            self.find_and_wait_element(locator)
        except selenium_exceptions:
            result = False
        else:
            result = True
        return result

    def get_current_url(self):
        try:
            current_url = self.driver.current_url
        except selenium_exceptions:
            current_url = 'None'
        return current_url

    def get_title_text(self):
        try:
            current_title = self.driver.title
        except selenium_exceptions:
            current_title = 'None'
        return current_title

    def go_to_page(self, url="/"):
        self.driver.get(url)

    def auth_by(self, login, password, timeout=1):
        self.find_and_wait_element(LoginPageLocators.login_input).send_keys(login)
        self.find_and_wait_element(LoginPageLocators.password_input).send_keys(password)
        self.find_and_wait_element(LoginPageLocators.accept_btn).click()
        sleep(timeout)  # just sleep. default is 1sec, but for positives auth need about 10sec

    def auth_by_admin(self):
        login_admin = cfg.user_admin["login"]
        password_admin = cfg.user_admin["password"]
        self.auth_by(login=login_admin, password=password_admin)

    def clear_session(self):
        sleep(1)
        print('\nclear session')
        a = self.driver.execute_script("return localStorage.clear();")
        print("return localStorage", a)
        sleep(7)
        x = self.driver.execute_script('setTimeout(function( ) { alert(\"storage cleared\"); }, 1000);')
        sleep(1)
        b = self.driver.execute_script('window.alert = () => 0')
        a = self.driver.execute_script("return localStorage.clear();")
        print("return localStorage", a)
        sleep(3)

    def logout_session(self):
        profile_prebutton = self.find_and_wait_element(LoginPageLocators.profile_widget)
        profile_prebutton.click()
        logout_button = self.find_and_wait_element(LoginPageLocators.logout_btn)
        logout_button.click()
        sleep(2)
