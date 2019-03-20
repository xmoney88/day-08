import page
from base.base_bainianaolai import BaseBaiNianAoLai


class PageBaiNianAoLai(BaseBaiNianAoLai):
    # 我的
    def page_me(self):
        self.base_click(page.login_me)

    # 已有账号,去登陆
    def page_existing_account(self):
        self.base_click(page.login_yiyou_zhanghao)

    # 用户名
    def page_username(self, username):
        self.base_input(page.login_username, username)

    # 密码
    def page_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    def page_click_login(self):
        self.base_click(page.login_click_login)

    # 设置
    def page_click_setting(self):
        self.base_click(page.login_setting)

    # 拖拽内存清理--修改密码
    def page_drag_and_drop(self):
        el1=self.base_find_element(page.login_clean_up)
        el2=self.base_find_element(page.login_set_pwd)
        self.base_drag_and_drop(el1,el2)

    # 退出
    def page_exit(self):
        self.base_click(page.login_exit)

    # 确定
    def page_yes(self):
        self.base_click(page.login_yes)