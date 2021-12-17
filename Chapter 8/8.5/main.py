import random
from breezypythongui import EasyFrame

class GuessingGame(EasyFrame):
  def __init__(self):
    EasyFrame.__init__(self, title = "The Guessing Game")
    self.lowerBound = 1;
    self.upperBound = 100;
    self.count = 0;
    self.myNumber = (self.lowerBound + self.upperBound) // 2;
    guess = "Is the number " + str(self.myNumber) + "?";
    self.myLabel = self.addLabel(text = guess, row = 0, column = 0, sticky = "NSEW", columnspan = 4);
    self.small = self.addButton(text = "Too small", row = 1, column = 0, command = self.goLarge);
    self.large = self.addButton(text = "Too large", row = 1, column = 1, command = self.goSmall);
    self.correct = self.addButton(text = "Correct", row = 1, column = 2, command = self.goCorrect);
    self.newGame = self.addButton(text = "New Game", row = 1, column = 3, command = self.goNewGame);

  def goLarge(self):
    self.count += 1;
    self.lowerBound = self.myNumber + 1;
    self.myNumber = (self.lowerBound + self.upperBound) // 2;
    self.myLabel["text"] = "Is the number you're thinking of " + str(self.myNumber) + "?";

  def goSmall(self):
    self.count += 1;
    self.upperBound = self.myNumber - 1;
    self.myNumber = (self.lowerBound + self.upperBound) // 2;
    self.myLabel["text"] = "Is the number " + str(self.myNumber) + "?";

  def goCorrect(self):
    self.large["state"] = "disabled";
    self.small["state"] = "disabled";
    self.correct["state"] = "disabled";

  def goNewGame(self):
    self.large["state"] = "normal";
    self.small["state"] = "normal";
    self.correct["state"] = "normal";
    self.lowerBound = 1;
    self.upperBound = 100;
    self.count = 0;
    self.myNumber = (self.lowerBound + self.upperBound) // 2;
    self.myLabel["text"] = "Is the number " + str(self.myNumber) + "?";

g1 = GuessingGame();
