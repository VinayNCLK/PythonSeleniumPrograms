
import pytest

@pytest.fixture()
def setup():
    print("Setup function is called")

def test_methodA(setup):
    print("Method1A is executed")


def test_methodB(setup):
    print("MethodB is executed")