from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_equal_product_name(self):
        product_name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_alert = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text
        assert product_name == product_name_in_alert, 'Product name does not match'

    def should_be_equal_product_price(self):
        product_price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_alert = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT).text
        assert product_price == product_price_in_alert, 'Product price does not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_SUCCESS_MESSAGE), \
            'Success message is presented, but should not be'

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_SUCCESS_MESSAGE), \
            'Success message should be disappeared'
