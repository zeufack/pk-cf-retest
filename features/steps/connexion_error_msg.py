from behave import *

from pages.connexion_error import ConnectionError


@given('navigate to carrefour web site')
def step_impl(context):
    context.connexion_error = ConnectionError(browser=context.driver)
    context.connexion_error.load()


@when('try to connet')
def step_impl(context):
    context.connexion_error.connect()


@then('the error message shoul be clear')
def step_impl(context):
    con_error_msg = context.connexion_error.get_connexion_error()
    assert con_error_msg != 'Error 16'



