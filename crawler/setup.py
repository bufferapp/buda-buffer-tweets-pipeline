# setup.py
import setuptools
REQUIRED_PACKAGES = []
PACKAGE_NAME = 'buda_buffer_tweets_crawler'
PACKAGE_VERSION = '0.0.1'

setuptools.setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='Crawler for Buda Buffer Tweets Pipeline',
    install_requires=REQUIRED_PACKAGES,
    packages=['crawler'],
    entry_points={
            'console_scripts': ['crawler=crawler.main:run']
    }
)
