iterations = int(input("Please enter the number of iterations desired: "))
add_this = 0
for i in range(1, iterations + 1, 2):
  if i % 4 == 1:
    add_this += 1/i
  else:
    add_this -= 1/i 
    pi = 4 * add_this
print("Estimated value based on inputted number of iterations inputted is " + str(pi))
