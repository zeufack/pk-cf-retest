from behave import *
from pages.payment_method_error import PaymentMethodError


@given("you are connect on carrefour market and you are log in to your account")
def step_impl(context):
    context.payment_method_error = PaymentMethodError(context.browser)
    context.payment_method_error.load()
    context.payment_method_error.connect()
    context.payment_method_error.fill_connection_form()


@when("navigate to payment method")
def step_impl(context):
    context.payment_method_error.navigate_to_payment_method()


@then("you should have an input for payment method")
def step_impl(context):
    assert context.payment_method_error.test_payment_input() is True
