import os, sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from pages.login_page import LoginPage
import pytest
from base.base_data import get_data


def get_login_data(key):
    return get_data('login_data', key)


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.login_page = LoginPage(self.driver)

    @pytest.mark.parametrize("args", get_login_data("test_login1"))
    def test_login1(self, args):
        self.login_page.click_my_button()
        self.login_page.click_sign_in_and_sign_up_button()
        self.login_page.input_username(args['username'])
        self.login_page.input_password(args['password'])
        self.login_page.click_login_button()
        assert self.login_page.is_toast_exit(args['toast'])

    @pytest.mark.parametrize("args", get_login_data("test_login2"))
    def test_login2(self, args):
        self.login_page.click_my_button()
        self.login_page.click_sign_in_and_sign_up_button()
        self.login_page.input_username(args['username'])
        self.login_page.input_password(args['password'])
        self.login_page.click_login_button()
        assert self.login_page.is_toast_exit(args['toast'])
