from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def new_driver():
    """
    creates webdriver instance of firefox
    """
    options = Options()
    # options.headless = True
    driver =  webdriver.Firefox(options=options)
    addon_path = 'C:\\Users\\kusha\\OneDrive\\Desktop\\project\\youtube cmd\\adblockultimate@adblockultimate.net.xpi'
    driver.install_addon(addon_path,temporary=True)
    return driver