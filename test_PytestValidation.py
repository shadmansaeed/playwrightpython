# fixtures
import pytest


@pytest.fixture(scope="module")  # scope= 'module' dile sudhu 1 bar firste eita run hobe r function dile jotobar linkage hobe totobar run hobe
def preWork():
    print("I setup module instance")
    return "pass"


@pytest.fixture(scope="function")  # scope= 'module' dile sudhu 1 bar firste eita run hobe r function dile jotobar linkage hobe totobar run hobe
def secondWork():
    print("I setup secondWork instance")
    yield  # pause
    print("tear down validation")


def test_initialCheck(preWork, secondWork):
    print("This is first test")
    assert preWork == "pass"


def test_SecondCheck(preSetupWork, secondWork):
    print("This is second test")
