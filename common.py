from code.config import Desired

driver = Desired().driver


def editText(id, text):
    box = driver.find_element_by_id(id)
    box.click()                # 点击输入框
    driver.keyevent(123)       # 光标移至最后
    box.clear()                # 清空输入框中的内容
    box.send_keys(text)        # 输入内容：text

