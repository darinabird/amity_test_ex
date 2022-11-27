from common.maintanance import BaseMethods
from common.locators import LoginPageLocators


class LoginHelper(BaseMethods, LoginPageLocators):
    def do_login_by_admin(self):
        self.auth_by_admin()

    def do_clear_session(self):
        self.clear_session()

    def do_logout(self):
        self.logout_session()
