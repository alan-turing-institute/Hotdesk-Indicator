from setuptools import setup, find_packages

setup(
    name="hotdesk_indicator",
    version="0.1",
    packages=find_packages(),
    install_requites=[
        "inky",
        "font-source-sans-pro"
        ],
    entry_points={
        "console_scripts": [
            "hotdesk-indicator = hotdesk_indicator.__main__:main"
            ]
        }
    )
