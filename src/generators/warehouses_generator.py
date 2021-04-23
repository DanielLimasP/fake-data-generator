from colors import LIGHT_GRAY, GREEN, RED, CYAN
from constants import WAREHOUSES_URL
from faker import Faker
import requests as req


def post_warehouse(
    token,
    name,
    country,
    state,
    city,
    zipi,
    neighborhood,
    street,
    extNumber,
    intNumber,
    phone,
    cellphone,
    observations,
    status,
    createdAt,
    updatedAt,
    warehouseType_id,
    userInCharge_id,
):
    res = req.post(
        WAREHOUSES_URL,
        json={
            "name": name,
            "country": country,
            "state": state,
            "city": city,
            "zip": zipi,
            "neighborhood": neighborhood,
            "street": street,
            "extNumber": extNumber,
            "intNumber": intNumber,
            "phone": phone,
            "cellphone": cellphone,
            "observations": observations,
            "status": status,
            "createdAt": createdAt,
            "updatedAt": updatedAt,
            "warehouseType_id": warehouseType_id,
            "userInCharge_id": userInCharge_id,
        },
        headers={"x-token": token},
    )

    return res.json()


def post_warehouses(token, count):
    fake = Faker()
    for n in range(count):
        name = fake.company()
        country = fake.country()
        state = fake.city_suffix()
        city = fake.city()
        zipi = fake.postcode()
        neighborhood = fake.street_suffix()
        street = fake.street_address()
        extNumber = fake.building_number()
        intNumber = extNumber
        phone = fake.phone_number()
        cellphone = fake.phone_number()
        observations = fake.catch_phrase()
        status = 1
        createdAt = "2020-04-20 16:20:00"
        updatedAt = "2020-04-20 16:20:00"
        warehouseType_id = 1
        userInCharge_id = 5

        post_warehouse(
            token,
            name,
            country,
            state,
            city,
            zipi,
            neighborhood,
            street,
            extNumber,
            intNumber,
            phone,
            cellphone,
            observations,
            status,
            createdAt,
            updatedAt,
            warehouseType_id,
            userInCharge_id,
        )
        print(GREEN, "POSTING Warehouse ", CYAN, "{}".format(name), LIGHT_GRAY)
    print()
    print(
        RED,
        "POSTED {} Warehouses to {}".format(n + 1, WAREHOUSES_URL),
        LIGHT_GRAY,
    )
