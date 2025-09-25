# fixtures
import pytest


@pytest.fixture(scope="module")  # scope= 'module' dile sudhu 1 bar firste eita run hobe r function dile jotobar linkage hobe totobar run hobe
def preWork():
    print("I setup module instance")


def test_initialCheck(preWork):
    print("This is first test")


def test_SecondCheck(preSetupWork):
    print("This is second test")
