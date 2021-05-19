from behave import *
from pages.translation_error import TranslationError


@given("you are on carrefour landing page")
def step_impl(context):
    context.translation_error = TranslationError(context.browser)
    context.translation_error.load()


@when("you scroll down to drive section")
def step_impl(context):
    context.translation_error.scrooll_down()


@then("you should have femmes enceintes instead of common.pregnant-women")
def step_impl(context):
    assert "Femmes enceintes" in context.translation_error.verify_test()
