from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="package_name_probably_on_pip",
    version="1.0.0",
    description="description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/repo",
    author="your_username",
    author_email="example@email.com",
    license="MIT",
    packages=["import_name"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "your",
        "package",
        "requirements",
    ],
)
