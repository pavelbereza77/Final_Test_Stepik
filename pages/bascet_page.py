from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):

    def form_cart(self):
        assert self.is_not_element_present(*MainPageLocators.CART_FORM)

    def should_text_basket_empty(self):
        text = self.browser.find_element(*MainPageLocators.TEXT_CART).text
        assert 'Ваша корзина пуста' in text, 'No text stating that the trash is empty'
