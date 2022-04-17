import pytest
#Hook function below which works on the framework level

def pytest_runtest_setup(item):
    #Called for running each tests in a directory
    print("\n************Setting up**************",item)


def pytest_cmdline_main(config):
    print("\n*********pytest_cmdline_main Hook*********")
    print(config.option)
    print(config.getoption("debug"))
    print(config.getoption("showcapture"))
    print(config.getoption("plugins"))
