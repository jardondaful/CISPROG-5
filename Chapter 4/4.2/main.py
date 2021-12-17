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
  
encryptedText = input("Please enter the message you want to be decrypted: ")
distance = int(input("Please enter the distance value: "))
print("Encrypted text: " + encryptedText) 
print("Shift: " + str(distance)) 
print("Decrypted text: " + decrypt(encryptedText,distance))
