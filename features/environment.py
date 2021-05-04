from behave import fixture, use_fixture
from helpers.browser_factory import get_browser


@fixture
def browser(context):
    context.browser = get_browser(context.browser_name)
    yield context.browser
    context.browser.quit()


def before_tag(context, tags):
    if 'proxy' in context.tags:
        context.browser_name = 'chrome_proxy'
    elif 'chrome' in context.tags:
        context.browser_name = 'chrome'
    else:
        context.browser_name = 'firefox'


def before_feature(context, feature):
    use_fixture(browser, context)
