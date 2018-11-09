from appium import webdriver
from time import sleep


class Desired():
    desired_caps = {}
    desired_caps['automationName'] = 'Appium'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['platformName'] = 'android'
    desired_caps['platformVersion'] = '8.0'    
    desired_caps['appPackage'] = 'com.abc.def'
    desired_caps['appActivity'] = '.ui.abc.LoginActivity'
    desired_caps['noReset'] = True        # 是否重新安装app  True则不重新安装
    
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(5)


class Account():
    user = 'dly'
    psw = 'you123'

