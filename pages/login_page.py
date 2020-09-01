from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):

    my_button = By.XPATH, ["text,我的", "resource-id,com.tpshop.malls:id/mine_tv"]
    sign_in_and_sign_up_button = By.ID, "com.tpshop.malls:id/head_img"
    username_area = By.XPATH, "text,请输入账号,1"
    password_area = By.XPATH, ["resource-id,com.tpshop.malls:id/pwd_et", "class,android.widget.EditText"]
    login_button = By.XPATH, ["text,登录", "resource-id,com.tpshop.malls:id/login_tv"]
    toast_password_wrong = By.XPATH, "text,密码错误"

    def click_my_button(self):
        self.click(self.my_button)

    def click_sign_in_and_sign_up_button(self):
        self.click(self.sign_in_and_sign_up_button)

    def input_username(self, username):
        self.input_text(self.username_area, username)

    def input_password(self, password):
        self.input_text(self.password_area, password)

    def click_login_button(self):
        self.click(self.login_button)
