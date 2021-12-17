d_c_n=int(input('Enter a decimal integer: '))
i = 1
o_c_n = 0
num=""
while (d_c_n != 0):
    rm = d_c_n % 8
    d_c_n //= 8
    o_c_n = o_c_n + rm * i
    i *= 10
    num = str(rm)+num
print('The octal representation is ',o_c_n)
