import pytest
import platform
from selenium import webdriver

sys_info = platform.platform()

'''
# scope=session - for the only one a browser instance start for all test suite
# scope=function - for many browsers (1 browser per test)
'''


@pytest.fixture(scope="class")
def browser():
    print("initiating chrome driver")
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    options.headless = False
    chrome_driver_binary = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    print("\nquit browser...")
    driver.close()
