from behave import given, when, then
import sys
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CDM
from selenium.webdriver.chrome.service import Service as Svc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import allure
import time


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage


@given("I am on the login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)

@when("I enter valid username and password")
def step_enter_valid_credentials(context):
    context.login_page.enter_username("sakshinitnaware17@gmail.com")
    context.login_page.enter_password("SAKSHIw@1234")

@when('I enter invalid username "{wronguser}" and password "{wrongpass}"')
def step_enter_invalid_credentials(context, wronguser, wrongpass):
    context.login_page.enter_username(wronguser)
    context.login_page.enter_password(wrongpass)

@when("I click the login button")
def step_click_login_button(context):
    context.login_page.click_login()

@then("The username field should be enabled")
def step_username_field_enabled(context):
    context.login_page.username_field_enabled()

@then("The password field should be enabled")
def step_password_field_enabled(context):
    context.login_page.password_field_enabled()

@then("The login button should be clickable")
def step_login_check(context):
    context.login_page.is_login_button_clickable()

@then("I should be redirected to the dashboard")
def step_verify_dashboard(context):
    assert context.login_page.check_dashboard_text().is_displayed(), "Dashboard not displayed"

@when("I logout from the application")
def step_logout(context):
    context.login_page.logout()

@then("I should see the login page again")
def step_back_to_login_page(context):
    try:
        assert context.login_page.is_login_button_clickable(), "Login button is not clickable"
    except TimeoutException:
        assert False, "Login page did not load after logout"

@then("I should see an error message")
def step_error_message_displayed(context):
    assert context.login_page.error_msg(), "no error msg"