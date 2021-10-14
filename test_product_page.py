from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.should_be_equal_product_name()
    page.should_be_equal_product_price()
