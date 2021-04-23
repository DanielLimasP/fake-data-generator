import requests as req
from constants import AUTH_URL, USER, PASSWORD

def login():
    res = req.post(
        AUTH_URL,
        json={"userName": USER, "password": PASSWORD},
    )
    return res.json()