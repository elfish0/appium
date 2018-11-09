from code.config import Desired

appPackage = Desired().desired_caps.get('appPackage')


def uninstall(app):
    Desired().driver.remove_app(app)
    print("已成功卸载：", app)


uninstall(appPackage)
