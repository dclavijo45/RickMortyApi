import bcrypt
import random

def encrypt(string, rtn="string"):
    s = random.randint(5, 10)
    salt = bcrypt.gensalt(s)
    hashed = bcrypt.hashpw(bytes(str(string), encoding="utf-8"), salt)

    if rtn == "string":
        return hashed.decode("utf-8")
    elif rtn == "byte":
        return hashed
    else:
        return hashed.decode("utf-8")

def decrypt(EncValidate, EncCompare):
    return bcrypt.checkpw(
        bytes(str(EncValidate), encoding="utf-8"),
        bytes(str(EncCompare), encoding="utf-8"),
    )