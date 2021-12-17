input_filename = input('Enter an input file name of your choice, including the extension: ')
file1 = open(input_filename, "w+")
L = ["Hello fellow user! \n", "Check out the contents of the output file you created! \n", "In the output file (which could be this file), every line is the same as in the input file but each line is numbered!"]
file1.writelines(L)
file1.close()
output_filename = input('Enter an output file name of your choice, including the extension: ')
file2 = open(output_filename, 'w+')
file2.close()
with open(input_filename, 'r') as f, open(output_filename, 'w') as w:
    number = 0
    for line in f:
        number += 1
        w.write('{:>4}> {}'.format(number, line))
print('\n \n')
print("These are the contents of the input file (named " + input_filename + "):")
print('')
with open(input_filename, 'r') as i:
    print(i.read())
print('\n \n')
print("These are the contents of the output file (named " + output_filename + "):")
print('')
with open(output_filename, 'r') as i:
    print(i.read())
