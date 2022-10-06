from setuptools import setup

# Dependencies are in setup.py for GitHub's dependency graph.
setup(
    install_requires=["Flask >= 2.1.0", "tinydb >= 4.0.0"],
    extras_require={"yaml": ["pyyaml >= 6.0"]},
)
