import math
tolerance = 0.00001

def newton(num):
  estimate = 1.0
  while True:
    estimate = (estimate + num/estimate)/2
    difference = abs(num-estimate**2)
    if difference<=tolerance:
      break
  return estimate

def main():
  x = input("Enter a positive number or press the enter/return key to quit: ")
  while True:
    if x=="":
      print("\nThanks for using the program!")
      break
    x = float(x)
    print("Newton's method of calculating the square root of", x, "yields an estiamte of", newton(x))
    print("Python's estimate of the square root of", x, "is", math.sqrt(x))
    x = input("\nEnter a positive number or press the enter/return key to quit: ")
    
main()
