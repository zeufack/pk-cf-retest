from behave import *
from pages.scrool_to_top_error import ScrollToTopError


@given('navigate to carrefour bio website sidenav')
def step_impl(context):
    context.scroll_error = ScrollToTopError(browser=context.driver)
    context.scroll_error.load()


@when('select the sidenav filter')
def step_impl(context):
    context.scroll_error.mouve_to_filter()


@then('the page shoul not scroll to top')
def step_impl(context):
    assert context.scroll_error.listen_to_scroll() is False


