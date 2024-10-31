from setuptools import setup, find_packages

setup(
    name = "Battleships",
    version = "1.0",
    packages = find_packages(),
    install_requires = [
        "flask >= 2.2.2",              
        "pytest >= 7.4.0",
    ],
)