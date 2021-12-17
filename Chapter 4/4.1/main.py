def encrypt(plainText,distance): 
    result = "" 
    for i in range(len(plainText)): 
        char = plainText[i] 
        if (char.isupper()): 
            result += chr((ord(char) + distance-65) % 26 + 65) 
        else: 
            result += chr((ord(char) + distance - 97) % 26 + 97) 
    return result 
  
plainText = input("Please enter the plaintext you want to be encrypted: ")
distance = int(input("Please enter the distance value: "))
print("Plaintext: " + plainText) 
print("Shift: " + str(distance)) 
print("Encrypted text: " + encrypt(plainText,distance)) 
