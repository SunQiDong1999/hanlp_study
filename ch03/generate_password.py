import random
import string

a = string.ascii_letters + string.digits
key = []


def generate_password(length=8) -> string:
    password_list = random.sample(a, length)
    password = "".join(password_list)
    return password


if __name__ == '__main__':
    for i in range(1000):
        print(generate_password())
