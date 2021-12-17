import random
def playRound(budget: int) -> tuple:
  sum = sumOfDice(random.randint(1,6), random.randint(1,6))
  if sum == 7:
    budget += 4
    return ("Win",budget)
  else:
    budget -= 1
    return ("Loss",budget)
def sumOfDice(die1: int, die2: int) -> int:
  return die1 + die2
def haveMoney(budget: int) -> bool:
  return True if budget > 0 else False
number_of_Rolls = 0
outputString = "\t{0}\t\t\t\t{1}\t\t\t\t\t{2}"
budget = int(input("Enter your gambling budget: "))
print("")
print("# of Rolls\t\tResult of Roll\t\tAmount left in pot")
print(outputString.format(number_of_Rolls, "Put", budget))
while haveMoney(budget):
    number_of_Rolls += 1
    output = playRound(budget)
    budget = output[1]
    print(outputString.format(number_of_Rolls, output[0], output[1]))
print("\nSorry, you're out of money. Thanks for playing!")    
