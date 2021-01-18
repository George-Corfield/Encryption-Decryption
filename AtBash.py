def encode(text):
    encrypted = ''
    for i in text:
        Lnum = (ord('Z')-ord(i))%26
        Lnum += ord('A')
        Lnew = chr(Lnum)
        encrypted += Lnew
    return encrypted

def decode(text):
    decrypted = ''
    for i in text:
        Lnum = (ord('Z')-ord(i))%26
        Lnum += ord('A')
        Lnew = chr(Lnum)
        decrypted += Lnew
    return decrypted

text = 'ZGYZHSRHIVEVIHV'
print(decode(text))

        
        
