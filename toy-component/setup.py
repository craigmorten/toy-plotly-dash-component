'''
setup.py
'''

from setuptools import setup

exec(open('toy_component/version.py').read())

setup(
    name='toy_component',
    version=__version__,
    author='craigmorten',
    packages=['toy_component'],
    include_package_data=True,
    license='MIT',
    description='A toy component for demo purposes',
    install_requires=[]
)
