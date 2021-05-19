from behave import *
from pages.gagnants_error import GagnantsError


@given("I am on carroufour website")
def step_impl(context):
    context.gagnants_error = GagnantsError(context.browser)
    context.gagnants_error.load()


@when("i click on the button to Display all the winner")
def step_impl(context):
    context.gagnants_error.nav_to_gagnants()


@then("i shoud have the list of winner")
def step_impl(context):
    assert context.gagnants_error.get_list_gagnants() != 'Not Found'
