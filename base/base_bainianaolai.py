from selenium.webdriver.support.wait import WebDriverWait


class BaseBaiNianAoLai():
    def __init__(self, driver):
        self.driver = driver

    # 定位元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda d: d.find_element(*loc))

    # 点击
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入+清空
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 拖拽
    def base_drag_and_drop(self, el1, el2):
        self.driver.drag_and_drop(el1, el2)

    # 获取文本
    def base_text(self, loc):
        return self.base_find_element(loc).text
