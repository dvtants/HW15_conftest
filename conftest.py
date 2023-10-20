import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

opts_chrome = ChromeOptions()
opts_firefox = FirefoxOptions()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="By default is 'chrome' name, but you can set --browser_name='firefox'")
    parser.addoption('--browser_mode', action='store', default="gui",
                     help="By default is 'gui' mode, but you can set --browser_mode='headless'")
    parser.addoption('--browser_window_size', action='store', default="standard",
                     help="By default is 'standard' window, but you can set --browser_window_size='max'")


@pytest.fixture(scope="function")
def browser(request):
    browser_mode = request.config.getoption("browser_mode")
    browser_name = request.config.getoption("browser_name")
    browser_window_size = request.config.getoption("browser_window_size")

    if browser_mode == "gui":
        print(f"\nbrowser_mode: {browser_mode}")
    elif browser_mode == "headless":
        opts_chrome.add_argument('--headless')
        opts_firefox.add_argument('--headless')
        print(f"\nbrowser_mode: {browser_mode}")
    else:
        print("The browser startup mode should be either 'gui' or 'headless'")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=opts_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=opts_firefox)
    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")

    if browser_window_size == "max":
        browser.maximize_window()
    elif browser_window_size == "standard":
        browser.set_window_size(600, 600)
    else:
        raise pytest.UsageError("--browser_window_size should be 'max' or 'standard'")

    yield browser
    print("\nquit browser..")
    browser.quit()



