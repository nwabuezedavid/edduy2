import uuid
import random

def genUdis(data):
    codegentrated = str(uuid.uuid4()).replace('-', "")[:data]
    return codegentrated
def referCode(data):
    codes = str(uuid.uuid4()).replace('-', "")[:data]
    return codes
def acc():
    code = random.randint(10**12, 10**13 - 1)
    return code

def generate_otp():
    otp = ""
    for i in range(4):
        otp += str(random.randint(0, 9))
    return otp