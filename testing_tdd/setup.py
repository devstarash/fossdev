from setuptools import setup, find_packages

setup(
    name="ndfl-starashchuk-v1",
    version="0.0.0",
    long_description="Tax ndfl calculator",
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
