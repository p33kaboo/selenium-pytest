import pytest

from .helpers import get_browser


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='Chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', default='en', help='Choose user language')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name").lower()
    language = request.config.getoption("language").lower()
    browser = get_browser(browser_name, language)
    browser.implicitly_wait(5)

    yield browser

    print("\nquit browser..")
    browser.quit()
