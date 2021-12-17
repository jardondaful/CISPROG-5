import math
side1 = int(input("Please enter the length of a side of a triangle: "))
print("\n")
side2 = int(input("Please enter the length of another side of the same triangle: "))
print("\n")
side3 = int(input("Please enter the length of the last side of the same triangle: "))
print("\n")
if(side3==math.sqrt(side1**2+side2**2) or side2==math.sqrt(side1**2+side3**2) or side1==math.sqrt(side2**2+side3**2)):
  print("This triangle is a right triangle")
else:
  print("This triangle is not a right triangle")
