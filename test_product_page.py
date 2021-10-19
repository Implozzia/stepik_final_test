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


@pytest.mark.negative
@pytest.mark.xfail(reason="Will be fixed later")
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.negative
def test_guest_cant_see_success_message(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.negative
@pytest.mark.xfail(reason="Will be fixed later")
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.should_disappeared_success_message()


@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()
