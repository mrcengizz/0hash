import base64
import hashlib
import sys
import optparse
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-c", "--cipher", dest="a", help="Enter cipher text")
    parse_object.add_option("-t", "--type", dest="types", help="Enter cipher type")
    return parse_object.parse_args()
def brute(types,a):
    def base(a):
        try:
            decoded = base64.b64decode(a)
            print("Base 64:",decoded.decode("utf-8"))
        except:
            pass
        try:
            decoded1= base64.b32decode(a)
            print("Base 32:",decoded1.decode("utf-8"))
        except:
            pass
        try:    
            decoded2 = base64.b16decode(a)
            print("Base 16",decoded2.decode("utf-8"))
        except:
            pass
        try:    
            decoded3 = base64.b85decode(a)
            print("Base 85",decoded3.decode("utf-8"))
        except:
            pass
    def rot(a):
        abc = "abcdefghijklmnopqrstuvwxyz"
        for dön in range(0,26):
            rot = "".join([abc[(abc.find(c)+dön)%26] for c in a])
            print("Rot"+str(dön)+" :",rot)

    def binary(a):
        #sorunlu bu
        degers = a.split()

        asciit = ""
        for deger in degers:
            aint = int(deger, 2)#buna bak
            print(aint)
            asciic = chr(aint)#ascii kodlar

            asciit += asciic
        print(asciit)
    def hexa(a):
        hexs = a[2:]
        byte = bytes.fromhex(hexs)
        asciis = byte.decode("ascii")
        print(asciis)
    if types == "base":
        base(a)
    elif types == "rot":
        rot(a)
    elif types == "binary":
        binary(a)
    elif types == "hex":
        hexa(a)

(user_input, arguments) = get_user_input()
brute(user_input.types, user_input.a)