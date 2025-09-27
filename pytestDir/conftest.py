import pytest

                                   # scope="session" means only run 1 time
@pytest.fixture(scope="session")  # scope= 'module' dile sudhu 1 bar firste eita run hobe r function dile jotobar linkage hobe totobar run hobe
def preSetupWork():
    print("I setup browser instance")