height = int(input("Enter the height from which the ball is dropped: "))
bounceIndex = float(input("Enter the bounciness index of the ball: "))
numberOfBounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
distance = 0
while numberOfBounces > 0:
  distance = distance + height
  height = height * bounceIndex
  distance = distance + height
  numberOfBounces-= 1
print("Total distance traveled is: " + str(distance) + "units.")
