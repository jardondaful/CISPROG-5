def convert_to_binary_string(number):
  bit_string = "{0:b}".format(number)
  return bit_string
string = input("Please enter a string: ")
bit_list = []
for i in string:
  bits = convert_to_binary_string(ord(i)+1)
  bits = bits[1:]+bits[0]
  bit_list.append(bits)
encrypted_string=""
for i in bit_list:
  encrypted_string+=i+" "
print("The following encrypted code adds 1 to each character's numeric ASCII value, converts it to a bit string, and shift the bits of this string one place to the left: " + encrypted_string)
