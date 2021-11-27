import bcrypt
import random

def encrypt(string, need="string"):
    s = random.randint(5, 10)
    salt = bcrypt.gensalt(s)
    hashed = bcrypt.hashpw(bytes(str(string), encoding="utf-8"), salt)

    if need == "string":
        return hashed.decode("utf-8")
    elif need == "byte":
        return hashed
    else:
        raise Exception("need must be 'string' or 'byte'")

def validate(EncValidate, EncCompare):
    return bcrypt.checkpw(
        bytes(str(EncValidate), encoding="utf-8"),
        bytes(str(EncCompare), encoding="utf-8"),
    )