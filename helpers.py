import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_browser(browser_name: str, user_language: str = 'es'):
    browser_name = browser_name.lower()

    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        browser = webdriver.Chrome(options=options)

    elif browser_name in ('mozilla', 'firefox'):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    print(f"\nstart {browser_name} browser for test..")
    return browser
