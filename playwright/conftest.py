import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope="session")
def user_credentials(request):  # here request is global parameter
    return request.param


@pytest.fixture(scope="session")

def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
