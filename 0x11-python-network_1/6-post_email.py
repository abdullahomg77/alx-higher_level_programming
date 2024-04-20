#!/usr/bin/python3
""" In url and email send post
displays body
"""

from sys import argv
import requests


if __name__ == "__main__":
    payload = {'email': argv[2]}
    req = requests.post(argv[1], data=payload)

    print(req.text)
