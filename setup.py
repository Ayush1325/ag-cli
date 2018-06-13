from setuptools import setup
setup(
    name='ad',
    version='0.0.1',
    packages=['ad'],
    install_requires=[
        'click',
        'inflection',
        'pystache'
    ],
    entry_points={
        'console_scripts': [
            'ad = ad.__main__:main'
        ]
    })
