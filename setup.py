from setuptools import setup
import sys

setup(name='Rester',
    version='1.0.1',
    author='Rajeev Chitamoor',
    author_email='rajeev@chitamoor.com',
    url='https://github.com/chitamoor/rester',
    license='LICENSE.txt',
    packages=['rester'],
    entry_points={
        'console_scripts':['apirunner = rester.apirunner:run']
    },
    test_suite="test",
    description='Rest API Testing',
    long_description=open('README.md').read(),
    install_requires=["requests", "testfixtures", "PyYAML>=3.9"],
    use_2to3= sys.version_info.major >= 3,
)

