from colors import LIGHT_GRAY, GREEN, RED, CYAN
import requests as req
from faker import Faker
from constants import USERS_URL


def post_user(
    token,
    name,
    lastNames,
    email,
    userName,
    password,
    userLogo,
    state,
    city,
    zipi,
    neighborhood,
    street,
    extNumber,
    intNumber,
    phone,
    cellphone,
    status,
    createdAt,
    updatedAt,
    role,
):
    res = req.post(
        USERS_URL,
        json={
            "name": name,
            "lastNames": lastNames,
            "email": email,
            "userName": userName,
            "password": password,
            "userLogo": userLogo,
            "state": state,
            "city": city,
            "zip": zipi,
            "neighborhood": neighborhood,
            "street": street,
            "extNumber": extNumber,
            "intNumber": intNumber,
            "phone": phone,
            "cellphone": cellphone,
            "status": status,
            "createdAt": createdAt,
            "updatedAt": updatedAt,
            "roles_idroles": role,
        },
        headers={"x-token": token},
    )

    return res.json()


def post_users(token, count):
    fake = Faker()
    for n in range(count):
        name = fake.name().upper()
        lastNames = fake.last_name().upper()
        email = fake.email()
        userName = fake.user_name().upper()
        password = "password"
        userLogo = "/public/img/users/test_img.jpg"
        state = fake.city_suffix()
        city = fake.city()
        zipi = fake.postcode()
        neighborhood = fake.street_suffix()
        street = fake.street_address()
        extNumber = fake.building_number()
        intNumber = extNumber
        phone = fake.phone_number()
        cellphone = fake.phone_number()
        status = 1
        createdAt = ("2020-04-20 16:20:00",)
        updatedAt = ("2020-04-20 16:20:00",)
        role = 2

        post_user(
            token,
            name,
            lastNames,
            email,
            userName,
            password,
            userLogo,
            state,
            city,
            zipi,
            neighborhood,
            street,
            extNumber,
            intNumber,
            phone,
            cellphone,
            status,
            createdAt,
            updatedAt,
            role,
        )
        print(GREEN, "POSTING User ", CYAN, "{}".format(name), LIGHT_GRAY)
    print()
    print(
        RED,
        "POSTED {} users to {}".format(n + 1, USERS_URL),
        LIGHT_GRAY,
    )
