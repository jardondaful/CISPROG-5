#Bank Account Info to try out this program
# Name: Jordan     PIN: 9860
# Name: Michelle   PIN: 9861
# Name: Melody     PIN: 9862
# Name: Amy        PIN: 9863
# Name: Jake       PIN: 9864

from bank import Bank, SavingsAccount

class ATM(object):
  def __init__(self, bank):
    self._account = None
    self._bank = bank
    self._methods = {} 
    self._methods["1"] = self._getBalance
    self._methods["2"] = self._deposit
    self._methods["3"] = self._withdraw
    self._methods["4"] = self._quit

  def run(self):
    failureCount = 0
    while True:
      userName=input("Enter Name : ")
      pin=input("Enter PIN : ")
      self._account=self._bank.get(pin)
      if(self._account==None) :
        print ("Error: unrecognized PIN\n")
        failureCount+=1
      elif(self._account.getName()!=userName) :
        print ("Error: unrecognized name\n")
        failureCount+=1
      else :
        self._processAccount()
    if(failureCount>=3) :
      print ("Third failed attempt. The cops have been called")
      return

  def _processAccount(self):
    while True:
      print("\n")
      print("1) View your balance")
      print("2) Make a deposit")
      print("3) Make a withdrawal")
      print("4) Quit\n")
      number = input("Enter a number to select an option: ")
      theMethod = self._methods.get(number, None)
      if theMethod == None: 
        print("Unrecognized number")
      else:
        theMethod()
      if self._account == None:
        break

  def _getBalance(self):
      print("Your balance is $", self._account.getBalance())

  def _deposit(self):
      amount = float(input("Enter the amount to deposit (without the dollar sign): "))
      self._account.deposit(amount)

  def _withdraw(self):
      amount = float(input("Enter the amount to withdraw (without the dollar sign): "))
      message = self._account.withdraw(amount)
      if message:
        print(message)

  def _quit(self):
      self._bank.save()
      self._account = None
      print("Have a nice day!")

def main():
  bank = Bank("bank.txt")
  atm = ATM(bank)
  atm.run()

def createBank(number = 0):
  bank = Bank()
  names = ["Jordan", "Michelle", "Melody", "Amy", "Jake"]
  for i in range(number):
    bank.add(SavingsAccount(names[i],str(9860 + i),100.00))
    bank.save("bank.txt")

createBank(5)

main()
