def GetKey(ciphertext, key):
    if len(key) == len(ciphertext):
        return(key)
    elif len(key) > len(ciphertext):
        return(key[0:len(ciphertext)])
    else:
        i = 0
        while len(key) < len(ciphertext):
            key+= key[i]
            i+=1
        return(key)

def encrypt(plaintext,key):
    encrypted = ''
    for i in range(len(plaintext)):
        Lnum = (ord(plaintext[i]) + ord(key[i]))%26
        Lnum += ord('A')
        Lnew = chr(Lnum)
        encrypted += Lnew
    return encrypted

def decrypt(ciphertext,key):
    decrypted = ''
    for i in range(len(ciphertext)):
        Lnum = (ord(ciphertext[i])-ord(key[i]))%26
        Lnum += ord('A')
        Lnew = chr(Lnum)
        decrypted += Lnew
    return decrypted

def FindKey(ciphertext, plaintext):
    key =''
    for i in range(len(ciphertext)):
        Lnum = (ord(ciphertext[i])-ord(plaintext[i]))%26
        Lnum += ord('A')
        Lnew = chr(Lnum)
        key += Lnew
    return key

plaintext = 'BEWARESUSPICIOUSLINKS'
ciphertext = 'GOADIBR'
key = 'CRACKING'

key =GetKey(ciphertext,key)
print(decrypt(ciphertext,key))
            
