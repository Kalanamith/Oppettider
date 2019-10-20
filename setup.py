import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements/req.txt") as f:
    install_requires = f.read().splitlines()

with open("requirements/test.txt") as f:
    test_requirements = f.read().splitlines()

with open("requirements/dev.txt") as f:
    dev_requirements = f.read().splitlines()


setuptools.setup(
    name="opening_hours",
    description="Restaurant opening hours in human readable format",
    long_description=long_description,
    version="0.0.1",
    install_requires=install_requires,
    extras_require={"test": test_requirements, "dev": dev_requirements},
    packages=setuptools.find_packages(),
    author="Kalanamith Mannapperuma",
    entry_points={"console_scripts": ["opening=opening_hours.cli:opening_hours_main"]},
    setup_requires=["pytest-runner"],
    test_suit="tests",
)
