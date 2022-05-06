from setuptools import setup
from flask_tinydb import __version__


def readme():
    with open("README.rst", encoding="utf8") as f:
        return f.read()


setup(
    name="Flask-tinydb",
    version=__version__,
    url="http://github.com/mmdbalkhi/flask-tinydb",
    license="BSD",
    author="Komeil Parseh",
    author_email="ahmdparsh129@gmail.com",
    description="flask-tinydb is a Flask extension that provides a TinyDB database.",
    long_description=readme(),
    long_description_content_type="text/x-rst",
    packages=["flask_tinydb"],
    py_modules=["flask_tinydb"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    python_requires=">=3.7",
    install_requires=["Flask", "tinydb", "pyyaml"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
