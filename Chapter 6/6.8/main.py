#Yes, the function defined by Lee is working good since whenever it is called on it prints out every element of the sequence. The recursive function printAll continuously calls on itself to print out the parameter's first element until the last element of the parameter is passed. Every time the function is called on, the parameter is changed so it contains all elements of the sequence except the first one. 
#The cost of using a recursive method is that it consumes more memory than using an iterative method (ex: a for loop). In an iterative method, it takes up only the necessary amount of memory. However, using a recursive method can consume a very large amount of memory and throw off the stability of the overall program if the sequence is long enough
def printAll(seq):
  if seq:
    print(seq[0])
    printAll(seq[1:])

def main():
  printAll("Python rules!\n")
  printAll((2,4,6,8))
  print("\n")
  printAll(['a','b','c','d'])
  print("\n")

main()
