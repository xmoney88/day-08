from selenium.webdriver.common.by import By

# 我
login_me = By.ID, "com.yunmall.lc:id/tab_me"
# 已有账号,去登陆
login_yiyou_zhanghao = By.ID, "com.yunmall.lc:id/textView1"
# 账号输入
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 密码
login_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 点击登录
login_click_login = By.ID, "com.yunmall.lc:id/logon_button"
# 点击设置
login_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 清理缓存
login_clean_up = By.ID, "com.yunmall.lc:id/setting_clear_cache"
# 修改密码
login_set_pwd = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
# 退出
login_exit = By.ID, "com.yunmall.lc:id/setting_logout"
# 确定
login_yes = By.ID, "com.yunmall.lc:id/ymdialog_right_button"
