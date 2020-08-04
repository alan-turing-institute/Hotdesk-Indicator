"""Setup script."""
from setuptools import setup, find_packages

setup(
    name="hotdesk",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
        "flask_bootstrap",
        "flask_migrate",
        "flask_restful",
        "flask_sqlalchemy",
        "flask_wtf"
    ],
)
