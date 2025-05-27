from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as Svc
from webdriver_manager.chrome import ChromeDriverManager as CDM
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

def before_all(context):
    options = Options()
    options.add_argument("--headless")  # Optional: remove if you want to see browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(service=Svc(CDM().install()), options=options)
    context.login_page = LoginPage(context.driver)

def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()