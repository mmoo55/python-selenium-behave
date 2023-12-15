from test_suite.test_base import TestBase



def before_scenario(context, driver):
    context.test = TestBase()
    context.test.setUp()

def after_scenario(context, driver):
    context.test.tearDown()

def after_step(context, step):
    print()