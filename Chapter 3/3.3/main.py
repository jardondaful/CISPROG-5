import math
smaller = int(input("Enter the smaller number: "))
print("\n")
larger = int(input("Enter the larger number: "))
print('\n')
count = 0
maxGuesses = round(math.log(larger - smaller + 1, 2))
while True: 
    count += 1 
    yourNumber = (smaller + larger) // 2 
    print("The computer just guessed that your number is " + str(yourNumber) + "\n")
    answer = input("Enter '= if the computer guessed correctly, '<' if the computer's guess is too low, or '>' if the comptuer's guess is too high: ") 
    if answer == "=": 
      print("\n")
      print("Hooray, the computer has guessed the correct number in", count, "tries!") 
      break 
    elif count == maxGuesses: 
      print("\n")
      print("I'm out of guesses because you cheated!") 
      break 
    elif answer == "<": 
      print("\n")
      larger = yourNumber - 1 
    else: 
      print("\n")
      smaller = yourNumber + 1
