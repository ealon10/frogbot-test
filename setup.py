from setuptools import setup, find_packages

setup(
    name='frogbot-test',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask==0.12.2',
        'requests==2.6.0',
        'urllib3==1.24.1',
        'pyyaml==3.13',
        'django==1.11.0',
    ],
)
