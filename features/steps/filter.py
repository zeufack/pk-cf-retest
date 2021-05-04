from behave import *
from pages.filter_error import FilterError


@given('i navigate to carrefour bio website')
def step_impl(context):
    context.filter_error = FilterError(browser=context.browser)
    context.filter_error.load()
    context.filter_error.handle_advertising(context.browser)


@when('i select Prix(croissant)filter')
def step_impl(context):
    context.filter_error.set_filter_decroissant()


@then('the product list shoul be sorted')
def step_impl(context):
    assert context.filter_error.get_categorie_sort_status() is not False
