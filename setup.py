from setuptools import setup, find_packages

setup(
    name="rest_api",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Flask==3.1.0",
        "marshmallow==3.26.1",
        "blinker==1.9.0",
        "click==8.1.8",
        "colorama==0.4.6",
        "itsdangerous==2.2.0",
        "Jinja2==3.1.6",
        "MarkupSafe==3.0.2",
        "packaging==24.2",
        "setuptools==76.0.0",
        "Werkzeug==3.1.3",
    ],
)
