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
    options.headless = False
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    print("\nquit browser...")
    driver.close()
