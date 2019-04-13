from setuptools import setup

setup(
    name="utilities-package",
    version="0.0.6",
    description="utilities package",
    url="https://github.com/terminal-labs/utilities-package",
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    license="license",
    packages=["utilities"],
    zip_safe=False,
    install_requires=["six", "bash", "termcolor"],
)
