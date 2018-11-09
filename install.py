from appium import webdriver


appPath = 'D:\work\\andriod_studio\\vis_apk\\2018-10-15_V2.1.5.apk'

def install(app_path):
    desired_caps = {}
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['platformName'] = 'android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['app'] = app_path
    desired_caps['appPackage'] = 'com.abc.def'
    desired_caps['appActivity'] = '.ui.abc.LoginActivity'
    desired_caps['noReset'] = True

    webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    print('已成功安装：', appPath)


if __name__ == '__main__':
    install(appPath)

