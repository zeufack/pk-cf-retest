from selenium import webdriver
from selenium.webdriver import Chrome
from behave import fixture, use_fixture


@fixture
def browser(context):
    with Chrome(executable_path='chromedriver') as context.driver:
        context.driver.implicitly_wait(10)
        yield context.driver
        context.driver.quit()


# def proxy_browser(context):
#     PORT = '178.32.129.31:3128'
#     options = webdriver.ChromeOptions()
#     options.add_argument('--proxy-server=%s' % PORT)
#     options.add_argument('--disable-extensions')
#     options.add_argument('--profile-directory=Default')
#     options.add_argument("--disable-plugins-discovery")
#     options.add_argument("--start-maximized")

#     with Chrome(options=options, executable_path='chromedriver') as context.proxy_driver:

#         context.proxy_driver.delete_all_cookies()
#         context.proxy_driver.set_window_position(0, 0)
#         context.proxy_driver.implicitly_wait(10)

#         yield context.proxy_driver

#         context.proxy_driver.quit()


def before_all(context):
    use_fixture(browser, context)
    # use_fixture(proxy_browser, context)


# def after_scenario(context, scenario):
#     context.driver.quit()
