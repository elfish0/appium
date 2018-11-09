from appium import webdriver
from time import sleep

user_id = 'com.abc.def:id/det_user'      # 账号输入框的resource-id
psw_id = 'com.abc.def:id/det_psd'        # 密码输入框的resource-id
user = 'dly'                             # 账号
psw = 'elf123'                           # 密码

def login(user_id,psw_id,user,psw):
    desired_caps = {}
    desired_caps['automationName']='Appium'
    desired_caps['deviceName']='Android Emulator'
    desired_caps['platformName'] = 'android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['noReset'] = True          # 是否重新安装app  True不重新安装
    desired_caps['appPackage'] = 'com.abc.def'       # 待测APP的appPackage
    desired_caps['appActivity'] = '.ui.abc.LoginActivity'     # 待测APP的appActivity
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(5)

    def editText(id, text):
        box = driver.find_element_by_id(id)
        box.click()              # 点击账号输入框
        driver.keyevent(123)     # 光标移至最后
        box.clear()              # 清空
        box.send_keys(text)      # 输入账号：text

    editText(user_id, user)
    editText(psw_id, psw)
    driver.find_element_by_id('com.abc.def:id/btn_login').click()

if __name__ == "__main__":
    login(user_id, psw_id, user, psw)