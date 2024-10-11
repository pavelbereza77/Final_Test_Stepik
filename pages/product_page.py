import time

from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):

    def should_be_product_add_cart(self):
        self.should_be_button_add_cart()
        self.add_product_cart()
        self.solve_quiz_and_get_code()
        self.should_be_massage_add_cart()
        self.name_product_message_must_product_name_cart()
        self.cost_basket_same_price_product()

    def should_be_button_add_cart(self):
        assert self.is_element_present(*ProductPageLocator.BUTTON_ADD_PRODUCT_CART), 'Not button add product cart'

    def add_product_cart(self):
        self.browser.find_element(*ProductPageLocator.BUTTON_ADD_PRODUCT_CART).click()

    def should_be_massage_add_cart(self):
        self.browser.implicitly_wait(5)
        assert self.is_element_present(*ProductPageLocator.MASSAGE_ADD_CART), 'Not massage add product cart'

    def name_product_message_must_product_name_cart(self):
        name_product = self.browser.find_element(*ProductPageLocator.NAME_PRODUCT).text
        name_product_cart = self.browser.find_element(*ProductPageLocator.NAME_PRODUCT_IN_MASSAGE).text
        assert name_product == name_product_cart, ('The name of the product in the message '
                                                   'does not match the product that was added to the cart')

    def cost_basket_same_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocator.PRICE_PRODUCT).text
        price_product_cart = self.browser.find_element(*ProductPageLocator.PRICE_IN_MASSAGE).text
        assert price_product == price_product_cart, 'The cost of the basket does not match the price of the product'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.NAME_PRODUCT_IN_MASSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_is_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocator.NAME_PRODUCT_IN_MASSAGE), \
            "Element is not disappeared"
