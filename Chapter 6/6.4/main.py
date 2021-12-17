import math
def limitReached(val, last):
  return abs(val-last)<0.00001

def improveEstimate(val, n):
  return (val+n/val)*0.5

def squareroot(n):
  val = n
  while True:
    last = val
    val = improveEstimate(val,n)
    if limitReached(val, last):
      break
  return val

def main():
  x = input("Enter a positive number or press the enter/return key to quit: ")
  while True:
    if x=="":
      print("\nThanks for using the program!")
      break
    x = float(x)
    print("Newton's method of calculating the square root of", x, "yields an estiamte of", squareroot(x))
    print("Python's estimate of the square root of", x, "is", math.sqrt(x))
    x = input("\nEnter a positive number or press the enter/return key to quit: ")
    
main()
