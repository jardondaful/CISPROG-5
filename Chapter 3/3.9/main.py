sum = 0
numbers = input("Please enter as many numbers as you want separated by spaces. Press enter when you are done: ")
map_object = numbers.split()
list_of_integers = list(map_object)
for i in range(len(list_of_integers)):
  sum += int(list_of_integers[i])
print("The sum of the numbers inputted is " + str(sum))
print("The avrage of the numbers inputted is " + str(1.0*(sum/len(list_of_integers))))
