from behave import *
from selenium.webdriver import Chrome

@given(u'Navigates to Facebook')
def step_impl(context):
    context.driver.get("https://www.facebook.com/")

@when(u'User enters username')
def step_impl(context):
    context.driver.find_element_by_id('email').send_keys("akshat.vohra@yahoo.com")

@when(u'User enters password')
def step_impl(context):
    context.driver.find_element_by_id('pass').send_keys("gattoo")

@when(u'User clicks on Login button')
def step_impl(context):
    context.driver.find_element_by_id('loginbutton').click()

@then(u'User logged into Facebook')
def step_impl(context):
    verify = context.driver.find_element_by_xpath("//span[contains(@class,'qtp')]").is_displayed()
    if verify:
        print("User Successfully logged to Facebook!!!!!")
    else:
        print("User not successfully logged to Facebook!!!!!")

@given(u'User is on login page')
def step_impl(context):
    print("HEllo")

@when(u'User enters "{site}"')
def step_impl(context,site):
    context.driver.get(site)
