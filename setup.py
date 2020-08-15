from setuptools import find_packages, setup


def read(file):
    with open(file) as f:
        return f.readlines()


setup(
    name='app',
    package=find_packages(),
    install_requires=read('requirements.txt'),
)
