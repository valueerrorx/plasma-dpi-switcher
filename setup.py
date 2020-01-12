from setuptools import setup, find_packages

setup(
    name='plasma-dpiswitch',
    version='0.1',
    packages=find_packages(exclude=('tests',)),
    scripts=['dpiswitch','dpiswitch-ui'],
    install_requires=open('requirements.txt').read()
)
