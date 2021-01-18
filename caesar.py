def encrypt():
    encoded = input('Cipher:')
    key = int(input('Key:'))
    decoded = ''
    for i in encoded.upper():
        num = ord(i)-65
        num = (num+key)%26
        newL = chr(num+65)
        decoded += newL
    print(decoded)

def KeyFind():
    encrypted = input('ciphertext:')
    decrypted = input('decrypted text')
    for i in range(0,26):
        newD = ''
        for j in encrypted.upper():
            num = ord(j)-65
            num = (num-i)%26
            newL = chr(num+65)
            newD += newL
        if newD == decrypted.upper():
            print(f'key = {i}')

def Brute():
    encrypted = input('cipher:')
    for i in range(0,26):
        decrypted =''
        for j in encrypted:
            num = ord(j)-65
            num = (num+i)%26
            newL = chr(num+65)
            decrypted += newL
        print(f'{decrypted}, key = {i}')
        

Brute()
    
