file1 = open("encrypt.txt", "r+")
encryptedText = file1.readline()
distance1 = int(file1.readline())
file2 = open("decrypt.txt", "r+")
decryptedText = file2.readline()
distance2 = int(file2.readline())
def encrypt(encryptedText, distance): 
    result = "" 
    for i in range(len(encryptedText)): 
        char =encryptedText[i] 
        if char == ' ':
          result += ' '
        elif (char.isupper()): 
            result += chr((ord(char) + distance-65) % 26 + 65) 
        else: 
            result += chr((ord(char) + distance - 97) % 26 + 97) 
    return result 

def decrypt(encryptedText,distance): 
    result = "" 
    distance = 26 - distance
    for i in range(len(encryptedText)): 
        char = encryptedText[i] 
        if (char.isupper()): 
            result += chr((ord(char) + distance-65) % 26 + 65) 
        else: 
            result += chr((ord(char) + distance - 97) % 26 + 97) 
    return result 
 


ex2 = open("outputForDecrypt.txt", "w")
ex2.write(decrypt(decryptedText, distance2))
ex2.close()
string2 = encrypt(encryptedText, distance1)
string2 = string2[:-1]
ex1 = open("outputForEncrypt.txt", "w")
ex1.write(encrypt(encryptedText, distance1))
ex1.close()
string1 = decrypt(decryptedText, 26-distance2)
string1 = string1[:-1]
print("Encrypted message from file that needed to be encrypted: " + string2)
print("Decrypted message from file that needed to be decrypted: " + string1)
  
