def convert_bits_to_string(a=''):
  return chr(int(a,2)-1)
def shift_bits_one_to_right(b=''):
  temp = list(b)
  new = (temp[-1:] + temp[0:-1])
  ret = ''
  for i in new:
    ret+=i
  return ret
encoded_string = input('Enter the encoded text:')
decoded_string = ''
for i in encoded_string.split():
  decoded_string+=convert_bits_to_string(shift_bits_one_to_right(i))
print("The decoded string is " + decoded_string)
