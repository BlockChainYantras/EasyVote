#!/usr/bin/python3

import sys
from authorityData import *

AUTH_PUBLIC_KEY_D = 35113647301148597661219974965825197099969499992771535637570104434838764280720273728159572193792057239555562654242774414087460201139277959866399250698600461422713156853556141667944933868036503097250086259006926979119504504598362872447156244183560794325858361366573965449134058365289067005307860927088206985473

def getSignedBlindedSecret(secret):
    signedBlindedSecret = pow(secret,  AUTH_PUBLIC_KEY_D, AUTH_PUBLIC_KEY_N)

    return hex(signedBlindedSecret)

if __name__ == '__main__':
    secret = int(sys.argv[1], 16)

    print(getSignedBlindedSecret(secret))
