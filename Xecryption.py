with open('Xecryption.txt','r') as f:
    Encrypted = f.read()
    Encrypted = Encrypted.split('.')

ASCII_value_list = []

for i in range(0,len(Encrypted)+1):
    ASCII_value = Encrypted[0]+Encrypted[1]+Encrypted[2]
    ASCII_value_list.append(ASCII_value)
    for x in [0,1,2]:
        Encrypted.pop(0)



print(ASCII_value_list)

    
