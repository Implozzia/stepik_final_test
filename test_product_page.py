from .pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('offer', ['0', '1', '2', '3', '4', '5', '6',
                                   pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(driver, offer):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}'
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_product_name()
    page.should_be_equal_product_price()
