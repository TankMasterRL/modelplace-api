# -*- coding: utf-8 -*-

from setuptools import setup

packages = ["modelplace_api"]

package_data = {"": ["*", "text_styles/*"]}
install_requires = [
    "pydantic==1.8.1",
    "loguru==0.5.1",
]

extras_require = {
    "vis": [
        "Pillow==7.1.2",
        "imageio==2.9.0",
        "sk-video==1.1.10",
        "pycocotools==2.0.2",
    ],
}

setup_kwargs = {
    "name": "modelplace-api",
    "version": "0.4.5",
    "description": "",
    "long_description": None,
    "author": "Xperience.ai",
    "author_email": "hello@xperience.ai",
    "maintainer": "Xperience.ai",
    "maintainer_email": "hello@xperience.ai",
    "url": None,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.7,<4.0",
    "extras_require": extras_require,
}

setup(**setup_kwargs)
