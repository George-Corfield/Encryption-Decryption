plain2morse = {'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}
morse2plain = {v:k for k, v in plain2morse.items()}

def MorseCode(text,plain2morse):
    encrypted = ''
    for i in text:
        if i == ' ':
            encrypted += '/'
        else:
            encrypted += plain2morse[i]
    return encrypted

def Decryptor(text,morse2plain):
    text = text.split('/')
    decrypted = ''
    for i in text:
        decrypted += morse2plain[i]
        decrypted += ' '
    return decrypted

ciphertext = '../-./..-./---/.-./--/.-/-/../---/-.'
print(Decryptor(ciphertext,morse2plain))

               
