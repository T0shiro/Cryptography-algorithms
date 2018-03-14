text = ""


def decrypt(text):
    for i in range(1, 26):
        print("+"+str(i)+" "+"".join([chr(ord(c) + i if ord(c)+i < 123 else ord(c)+i-26) for c in text]))

def encrypt(text, decal):
    print("".join([chr(ord(c) - decal if ord(c) - decal > 96 else ord(c) - decal + 26) for c in text]))

#decrypt("jyfwavnyhwoplhwwspxbll")
encrypt("cryptographieappliquee", 19)
