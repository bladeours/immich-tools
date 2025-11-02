from setuptools import setup, find_packages

setup(
    name="immich-tools",
    version="0.2.9",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["click", "requests", "PyExifTool", "pytest", "dacite"],
    entry_points={
        "console_scripts": [
            "immich-tools = src.cli:main",
        ],
    },
)
