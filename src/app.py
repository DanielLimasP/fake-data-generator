from generators.users_generator import post_users
from generators.warehouses_generator import post_warehouses
from login import login

if __name__ == "__main__":
    # Login
    token = login()["token"]
    print()
    # post_users(token, 1)
    post_warehouses(token, 10)
    print()
