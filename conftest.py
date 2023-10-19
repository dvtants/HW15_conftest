import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts_chrome = Options()


def pytest_addoption(parser):
    parser.addoption('--browser_mode', action='store', default="headless",
                     help="By default is headless mode, but you can set --browser_mode='gui'")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    options = opts_chrome
    options.add_argument('--start-maximized')
    browser_mode = request.config.getoption("browser_mode")
    if browser_mode == "gui":
        print(f"\nbrowser_mode: {browser_mode}")
    elif browser_mode == "headless":
        options.add_argument('--headless')
        print(f"\nbrowser_mode: {browser_mode}")
    else:
        print("Режим запуску браузера повинен бути або gui або headless")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
