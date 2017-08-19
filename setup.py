# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="sleepdog",
    packages=["sleepdog"],
    version="0.0.1",
    description="Slack bot for monitoring and notification of filesystem events.",
    author="yag_ays",
    author_email="yanagi.ayase@gmail.com",
    url="https://github.com/yagays/sleepdog",
    install_requires=["watchdog", "slacker"],
    entry_points={
        "console_scripts": [
            "sleepdog = sleepdog.sleepdog:main"
        ]
    }
)
