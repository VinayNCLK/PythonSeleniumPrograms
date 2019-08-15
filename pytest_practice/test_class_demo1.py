
import pytest


@pytest.mark.usefixtures("setup","onetime_setup")
class Test_Demo1():
    @pytest.fixture(autouse=True)
    def classSetup(self):
        print("Class level setup")

    def test_methodA(self):
        print("MethodA is executed")

    def test_methodB(self):
        print("MethodB is executed")

