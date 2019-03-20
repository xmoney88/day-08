from appium import webdriver


def GetDriver():

    # desired_caps为字典格式 - 常用参数：
    desired_caps = {}
    # 必填-且正确
    desired_caps['platformName'] = 'Android'
    # 必填-且正确
    desired_caps['platformVersion'] = '5.1'
    # 必填
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # APP包名
    desired_caps['appPackage'] = 'com.yunmall.lc'
    # 启动名---com.yunmall.lc/com.yunmall.ymctoc.ui.activity.MainActivity
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    # 不重置应用
    desired_caps["noReset"] = True
    # 解决中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
