from distutils.core import setup
from setuptools import setup, find_packages
setup(
        install_requires=[
            "jwcrypto>=1.0"
            ],
        entry_points={
            "console_scripts":[
                "genjwtkey=genjwtkey.generate:generate"
                ]
            },
        packages=find_packages()
        )

