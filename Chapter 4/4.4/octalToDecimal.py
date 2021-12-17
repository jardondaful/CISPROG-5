o_t_n=int(input('Enter a string of octal digits: '))
i = 1
dc = 0
while (o_t_n != 0):
    rmd = o_t_n % 10
    o_t_n //= 10
    dc += rmd * i
    i *= 8
print('The integer value is ',dc)
