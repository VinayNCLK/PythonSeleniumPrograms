
import pytest

@pytest.yield_fixture()
def setup():
    print("Setup function is called before test method")
    yield
    print("Setup function is called after test method")

def test_methodA(setup):
    print("MethodA is executed")


def test_methodB(setup):
    print("MethodB is executed")