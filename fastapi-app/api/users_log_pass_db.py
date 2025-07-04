import bcrypt


def hash_pass(password: str):
    salt = bcrypt.gensalt()
    pwd_bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


users_db = {
    "dmitri": {
        "username": "dmitri",
        "hashed_password": hash_pass("qwerty"),
        "salary": "110.000",
        "next_raise_at": "01.01.2026",
    },
    "max": {
        "username": "max",
        "hashed_password": hash_pass("password"),
        "salary": "200.000",
        "next_raise_at": "01.08.2026",
    },
    "olga": {
        "username": "olga",
        "hashed_password": hash_pass("1234567"),
        "salary": "80.000",
        "next_raise_at": "01.09.2025",
    },
}
