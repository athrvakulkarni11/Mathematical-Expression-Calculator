from setuptools import setup, find_packages

setup(
    name="expression-evaluator",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "fastapi",
        "uvicorn",
        "streamlit",
        "requests",
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "httpx",
            "tox",
        ],
    },
) 