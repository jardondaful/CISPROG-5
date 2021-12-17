input_filename = input('Enter an input file name of your choice, including the extension: ')
file1 = open(input_filename, "w+")
L = list()
num = input("Enter how many entries you want to make in the input file: ")
print('Enter the entries: ')
for i in range(int(num)):
    n = input()
    L.append(n)
file1.writelines(L)
file1.close()
print('')
output_filename = input('Enter an output file name of your choice, including the extension: ')
file2 = open(output_filename, 'w+')
file2.close()
with open(input_filename, 'r') as f, open(output_filename, 'w') as w:
    for line in f:
        w.write('{}'.format(line))
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
