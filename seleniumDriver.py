from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def new_driver():
    """
    creates webdriver instance of firefox
    """
    options = Options()
    options.headless = True
    return webdriver.Firefox(options=options) 