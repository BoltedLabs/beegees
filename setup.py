from setuptools import setup

setup(
    name='beegees',
    version='0.1',
    description='For those that need fresh beegees.',
    url='https://github.com/BoltedLabs/beegees',
    install_requires=[
        'click'
    ],
    scripts=['bins/beegees']
)
