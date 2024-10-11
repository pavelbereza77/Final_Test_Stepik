from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocator():
    BUTTON_ADD_PRODUCT_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")

    MASSAGE_ADD_CART = (By.CSS_SELECTOR, "#messages")

    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")
    NAME_PRODUCT_IN_MASSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    PRICE_IN_MASSAGE = (By.CSS_SELECTOR, '#messages :nth-child(3) strong')




