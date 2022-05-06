from setuptools import setup

def readme():
    with open("README.rst", encoding="utf8") as f:
        return f.read()


setup(
    install_requires=["Flask >= 2.1.0", "tinydb >= 4.0.0", "pyyaml >= 6.0"],
)
