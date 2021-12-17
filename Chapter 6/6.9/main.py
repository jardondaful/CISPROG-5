import functools
def main():
  file = open("integers.txt", 'r')
  file = file.read()
  file = file.split()
  file = list(map(int, file))
  print("The average of the numbers in the text file is ", functools.reduce(lambda x, y: x+y / len(file), file, 0))

main()
