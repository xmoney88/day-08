import os
import sys
sys.path.append(os.getcwd())
from base.get_driver import GetDriver
from page.page_biannianaolai import PageBaiNianAoLai


class TestLogin():
    def setup(self):
        self.driver = GetDriver()
        self.login = PageBaiNianAoLai(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_login(self, username="itheima", pwd="123456"):
        self.login.page_me()
        self.login.page_existing_account()
        self.login.page_username(username)
        self.login.page_pwd(pwd)
        self.login.page_click_login()
        self.login.page_click_setting()
        self.login.page_drag_and_drop()
        self.login.page_exit()
        self.login.page_yes()
