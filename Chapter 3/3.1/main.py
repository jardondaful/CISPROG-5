side1 = int(input("Please enter the length of a side of a triangle: "))
print("\n")
side2 = int(input("Please enter the length of another side of the same triangle: "))
print("\n")
side3 = int(input("Please enter the length of the last side of the same triangle: "))
print("\n")
if(side1==side2 and side1==side3 and side2==side3):
  print("This triangle is an equilateral triangle")
else:
  print("This triangle is not an equilateral triangle")
