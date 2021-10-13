import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru and etc")


@pytest.fixture(scope='function')
def driver(request):
    browser_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    print('\nstart browser for test')
    driver = webdriver.Chrome(options=options)
    yield driver
    print('\nquit browser')
    driver.quit()
