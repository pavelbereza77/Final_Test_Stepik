from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_CART_IN_MAIN_PAGE = (By.CSS_SELECTOR, '.btn-group .btn-default')
    CART_FORM = (By.CSS_SELECTOR, '.basket-items')
    TEXT_CART = (By.CSS_SELECTOR, '#content_inner p')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_ADDRESS = (By.NAME, "registration-email")
    PASSWORD_1 = (By.NAME, "registration-password1")
    PASSWORD_2 = (By.NAME, "registration-password2")
    BUTTON_REGISTER_USER = (By.NAME, 'registration_submit')


class ProductPageLocator():
    BUTTON_ADD_PRODUCT_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")

    MASSAGE_ADD_CART = (By.CSS_SELECTOR, "#messages")

    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")
    NAME_PRODUCT_IN_MASSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    PRICE_IN_MASSAGE = (By.CSS_SELECTOR, '#messages :nth-child(3) strong')
