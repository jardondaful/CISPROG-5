from die import Die
class Player(object):
  def __init__(self):
    self.die1 = Die()
    self.die2 = Die()
    self.roll = ""
    self.rollsCount = 0
    self.atStartup = True
    self.winner = self.loser = False

  def __str__(self):
    return self.roll

  def getNumberOfRolls(self):
    return self.rollsCount

  def rollDice(self):
    self.rollsCount += 1
    self.die1.roll()
    self.die2.roll()
    (v1, v2) = (self.die1.getValue(),
    self.die2.getValue())
    self.roll = str((v1, v2)) + " " + str(v1 + v2)
    if self.atStartup:
      self.initialSum = v1 + v2
      self.atStartup = False
      if self.initialSum in (2, 3, 12):
        self.loser = True
      elif self.initialSum in (7, 11):
        self.winner = True
    else:
      laterSum = v1 + v2
      if laterSum == 7:
        self.loser = True
      elif laterSum == self.initialSum:
        self.winner = True
    return (v1, v2)
  def isWinner(self):
    return self.winner

  def isLoser(self):
    return self.loser

  def play(self):
    while not self.isWinner() and not self.isLoser():
      self.rollDice()
    return self.isWinner()

def playOneGame():
  player = Player()
  while not player.isWinner() and not player.isLoser():
    player.rollDice()
    print(player)
  if player.isWinner():
    print("\nYou win!")
  else:
    print("\nYou lose...")

def playManyGames(number):
  wins = 0
  losses = 0
  winRolls = 0
  lossRolls = 0
  for count in range(number):
    player = Player()
    hasWon = player.play()
    rolls = player.getNumberOfRolls()
    if hasWon:
      wins += 1
      winRolls += rolls
    else:
      losses += 1
      lossRolls += rolls
  print("The total number of wins is", wins)
  print("The total number of losses is", losses)
  if wins!=0:
    print("The average number of rolls per win is %0.3f" % \
    (winRolls / wins))
  else:
    print("The average number of rolls per win is 0")
  if losses!=0:
    print("The average number of rolls per loss is %0.3f" % \
    (lossRolls / losses))
  else:
    print("The average number of rolls per loss is 0")
  print("The winning percentage is %0.3f" % (wins / number * 100) + "%")

def main():
  print("The displaying of the simulation of playing three separate games of craps: \n")
  print("______________\n")
  print("Game #1: \n")
  playOneGame()
  print("______________\n")
  print("Game #2: \n")
  playOneGame()
  print("______________\n")
  print("Game #3: \n")
  playOneGame()
  print("\n----------------------------------------------")
  print("\n\nThe results of a SEPARATE simulation of playing 8 games of craps: \n")
  playManyGames(8)

if __name__ == "__main__":
  main()
