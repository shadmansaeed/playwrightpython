# fixtures
import pytest


@pytest.fixture(scope="function")  # scope= 'module' dile sudhu 1 bar firste eita run hobe r function dile jotobar linkage hobe totobar run hobe
def preWork():
    print("I setup browser instance")


def test_initialCheck(preWork):
    print("This is first test")


def test_SecondCheck(preWork):
    print("This is second test")
