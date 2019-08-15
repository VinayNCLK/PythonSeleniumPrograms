
import pytest

@pytest.yield_fixture()
def setup():
    print("Setup function is called before test method")
    print("Login to app")
    yield
    print("Setup function is called after test method")
    print("Logout from the app")


@pytest.yield_fixture(scope="class")
def onetime_setup(browser):
    print("Setup function is called before test Module")
    if browser == "chrome":
        print("Execution will start in chrome browser")
    elif browser == "firefox":
        print("Execution will start in firefox browser")
    elif browser == "ie":
        print("Execution will start in ie browser")
    else:
        return False
    yield
    print("Setup function is called after test Module")
    print("Closing the browser")



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
