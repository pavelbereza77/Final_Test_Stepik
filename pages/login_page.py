from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        login_page = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        cur_url = self.browser.current_url
        assert cur_url in login_page.get_attribute("href"), 'Not correct url login page'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Not form login'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Not register_form'

    def should_field_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADDRESS), 'Not field input email address'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_1), 'Not field input email password_1'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_2), 'Not field input email password_2'
        assert self.is_element_present(*LoginPageLocators.BUTTON_REGISTER_USER), 'Not button register'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER_USER).click()
