from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver= webdriver.Chrome()
        print("Launching Chrome Browser........")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser.......")
    else:
        driver= webdriver.Ie()
    return driver
    #driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    if not hasattr(config, 'workerinput'):  # To ensure it's not running in a worker process
        config._metadata = {}  # Initialize the metadata dictionary

@pytest.hookimpl(optionalhook=True)

## Pytest HTML report
def pytest_metadata(config):
    config.metadata['Project Name'] = 'nop Commerce'
    config.metadata['Module Name'] = 'Customers'
    config.metadata['Tester'] = 'Pavan'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
