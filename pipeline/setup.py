# setup.py
import setuptools
REQUIRED_PACKAGES = []
PACKAGE_NAME = 'buda_buffer_tweets_pipeline'
PACKAGE_VERSION = '0.0.1'

setuptools.setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='Dataflow pipeline for the Buda Buffer Tweets Pipeline',
    install_requires=REQUIRED_PACKAGES,
    packages=['pipeline'],
    entry_points={
            'console_scripts': ['pipeline=pipeline.main:run']
    }
)
