from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CDM
from selenium.webdriver.chrome.service import Service as Svc
def step_impl(context) :
    context.driver = webdriver.Chrome(service=Svc(CDM().install))
    context.driver.get("<enter url>")
    context.driver.maximize_window()
    context.excel = ExcelUtil("<enetr path>")
    context.login_path = LoginPage(context.diver)

@when("Ï try to login with all data sets")
def setps_impl(context) :
    for  i in range(2,context.excel.get_row_count()+1) :
        username =context.excel.read_data(i,1)
        password= context.excel.read_data(i,2)