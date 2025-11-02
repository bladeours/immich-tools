from setuptools import setup, find_packages
import src

setup(
    name="immich-tools",
    version="0.2.7",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["click", "requests", "PyExifTool", "pytest", "dacite"],
    entry_points={
        "console_scripts": [
            "immich-tools = src.cli:main",
        ],
    },
)
