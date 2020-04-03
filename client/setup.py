"""Hotdesk Indicator."""
from setuptools import setup, find_packages

setup(
    name="hotdesk_indicator",
    version="0.1",
    packages=find_packages(),
    install_requites=[
        "inky",
        "font-source-sans-pro",
        "requests"
        ],
    entry_points={
        "console_scripts": [
            "hotdesk-set = hotdesk_indicator.scripts.set:main",
            "hotdesk-get = hotdesk_indicator.scripts.get:main"
            ]
        }
    )
