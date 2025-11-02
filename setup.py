from setuptools import setup, find_packages
import os

version = {}
with open(os.path.join("src", "immich_tools", "__init__.py")) as f:
    exec(f.read(), version)

setup(
    name="immich-tools",
    version=version["__version__"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["click", "requests", "PyExifTool", "pytest", "dacite"],
    entry_points={
        "console_scripts": [
            "immich-tools = immich_tools.cli:main",
        ],
    },
)
