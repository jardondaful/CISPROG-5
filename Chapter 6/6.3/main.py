import math
tolerance = 0.000001
def newton(num, estimate = 1.0):
  difference_value = abs(num-estimate**2)
  if difference_value<=tolerance:
    return estimate
  else:
    return newton(num, (estimate+num/estimate)/2)
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
