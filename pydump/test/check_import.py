import sys
import pip
import typing


def say_hello():
    print('Hello')


def print_pip_version():
    print(pip.__version__)


def print_python_version_info():
    print("Python version: {}.{}.{}".format(
        sys.version_info.major, sys.version_info.minor, sys.version_info.micro))


def check_typeguard_issue():
    # ref: https://github.com/microsoft/pyright/blob/main/docs/configuration.md
    if hasattr(typing, 'TypeGuard'):
        print('TypeGuard is available!')
    else:
        print('TypeGuard is not available.')
    print()


def all():

    print_python_version_info()
    print_pip_version()
    check_typeguard_issue()
