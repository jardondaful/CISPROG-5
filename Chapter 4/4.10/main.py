#use attatched file names to compare the files when using the program
file1 = input("Enter the name of the first file with its extension name: ")
file2 = input("Enter the name of the second file with its extension name:")
inputFile1 = open(file1, 'r')
inputFile2 = open(file2, 'r')
print("")
n = 0
while n == 0:
  line1 = inputFile1.readline()
  line2 = inputFile2.readline()
  if line1==line2:
    print("Yes \n")
  elif line1 != line2:
    print("No \n \n")
    print("Line from " + file1 + " that differs from " + file2 + ": " + line1 + "\n")
    print("Line from " + file2 + " that differs from " + file1 + ": " + line2 + " \n")
    break
