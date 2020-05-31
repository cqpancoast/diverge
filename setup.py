from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="qflip-CQPANCOAST",
    version="1.0.2",
    author="Casey Pancoast",
    description="Determinism is for losers - make your decisions using quantum mechanics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cqpancoast/quantum-flip",
    license="MIT",
    keywords="quantum coin flip rng qrng qflip flip universe",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics"
    ],
    entry_points={
        "console_scripts": [
            "qflip=qflip.qflip:main"
        ]
    }
)
