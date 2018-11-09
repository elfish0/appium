from code.config import Desired, Account
from code.common import editText

user_id = 'com.abc.def:id/det_user'      # 账号输入框的resource-id
psw_id = 'com.abc.def:id/det_psd'        # 密码输入框的resource-id
user = Account().user
psw = Account().psw

def login(user_id,psw_id,user,psw):
    driver = Desired().driver
    editText(user_id, user)
    editText(psw_id, psw)
    driver.find_element_by_id('com.abc.def:id/btn_login').click()

if __name__ == "__main__":
    login(user_id, psw_id, user, psw)



