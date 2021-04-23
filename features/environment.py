from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from behave import fixture, use_fixture


@fixture
def browser(context):
    with Chrome(executable_path='chromedriver') as context.driver:
        context.driver.implicitly_wait(10)
        yield context.driver
        context.driver.quit()


# @fixture
# def proxy_browser(context):
#     profile = FirefoxProfile()
#     profile.set_preference('network.proxy.type', 1)
#     profile.set_preference("network.proxy.http", "217.182.239.121")
#     profile.set_preference("network.proxy.http_port", "1000")
#     profile.update_preferences()
#     context.proxyed_browser = Firefox(
#         firefox_profile=profile, executable_path='geckodriver')
#     context.proxyed_browser.implicitly_wait(10)
#     yield context.proxyed_browser
#     context.proxy_browser.quit()


def before_all(context):
    use_fixture(browser, context)
