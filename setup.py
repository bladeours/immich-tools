from setuptools import setup, find_packages

setup(
    name="immich-tools",
    version="0.1.8",
    packages=find_packages(),
    install_requires=["click", "requests", "PyExifTool"],
    entry_points={
        "console_scripts": [
            "immich-tools = src.cli:main",
        ],
    },
)
