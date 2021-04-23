import pytest

from selenium.webdriver import Chrome
from pages.filter_error import FilterError
from pages.connexion_error import ConnectionError
from pages.scrool_to_top_error import ScrollToTopError


@pytest.fixture
def browser():
    with Chrome(executable_path='chromedriver') as driver:
        driver.implicitly_wait(10)
        yield driver
        driver.quit()


def test_categorie_filter(browser):
    filter_error = FilterError(browser)
    filter_error.load()
    assert filter_error.get_categorie_sort_status() == True


def test_connexion_msg(browser):
    con_error = ConnectionError(browser)
    con_error.load()
    con_error.connect()
    con_error_msg = con_error.get_connexion_error()
    assert con_error_msg != 'Error 16'


def test_sidenav_test(browser):
    scroll_error = ScrollToTopError(browser)
    scroll_error.load()
    scroll_error.mouve_to_filter()
    assert scroll_error.listen_to_scroll() == False


def test_flag_display(browser):
    pass
