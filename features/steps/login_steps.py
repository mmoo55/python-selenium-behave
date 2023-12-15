from behave import given, when, then, step


@given(u'Im on the webpage')
def given_im_on_the_webpage(context):
    print('INSIDE GIVEN')
    print('From context.test.setUp()')


@when(u'I enter valid credentials')
def when_i_put_my_credentials(context):

    print('INSIDE WHEN')
    login_section = context.test.login_section
    username = context.test.USERNAME
    password = context.test.PASSWORD

    print(username, password)

    login_section.login_label.click()
    login_section.email_textbox.set_text(username)
    login_section.password_textbox.set_text(password)
    login_section.login_button.click()


@then(u'I can see the whole page')
def then_i_can_see_the_whole_page(context):
    context.test.assertTrue(context.test.main_section.logout_button.control_is_displayed(), "It is not displayed")

    print('INSIDE THEN')

