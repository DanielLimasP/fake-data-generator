from requests.api import post
from faker import Faker
import requests as req

# ANSI Colors
LIGHT_GRAY = "\033[0;37m"
GREEN = "\033[0;32m"
RED = "\033[0;31m"
ITALIC = "\033[3m"

# Auth variables
USER = "ALERUN"
PASSWORD = "123456"

# Routes
AUTH_URL = "http://localhost:8000/api/auth/login"
USERS_URL = "http://localhost:8000/api/users"


def login():
    res = req.post(
        AUTH_URL,
        json={"userName": USER, "password": PASSWORD},
    )
    return res.json()


def postUser(name, email, userName, password, role):
    token = login()["token"]
    res = req.post(
        USERS_URL,
        json={
            "name": name,
            "email": email,
            "userName": userName,
            "password": password,
            "roles_idroles": role,
            "warehouse_idwarehouse": 1,
            "status": 1,
        },
        headers={"x-token": token},
    )

    return res.json()


def postUsers(count=10):
    fake = Faker()
    for n in range(count):
        postUser(fake.name(), fake.email(), fake.user_name(), "password", 2)
        print(GREEN, "POSTING User", LIGHT_GRAY)
    print()
    print(RED, "POSTED {} users to {}".format(n, USERS_URL), LIGHT_GRAY)


if __name__ == "__main__":
    # postUser("VALERIA", "test8@gmail.com", "VALTEST", "password", 2)
    postUsers()
