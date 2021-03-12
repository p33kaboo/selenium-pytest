from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_button = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        url = login_button.get_attribute('href')
        assert 'login' in url, 'second method: login link not found'

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM).is_displayed(), 'login page not found'

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM).is_displayed(), \
            'registration page not found'
