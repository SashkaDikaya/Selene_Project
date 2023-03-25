import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.timeout = 3.0
    yield
    browser.quit()
