#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="cipher-tools",
    version="3.5.0",
    description="Cipher Tools - Titan Suite (150 Precision Cybersecurity, Forensics & System Engineering Tools)",
    author="Cipher Engineering",
    license="MIT",
    py_modules=["cipher_tools", "test_suite"],
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "cipher-tools=cipher_tools:main",
        ],
    },
)
