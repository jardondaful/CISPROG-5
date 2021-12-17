import random
from cards import Card
class Deck(object):
  def __init__(self):
    self.cards = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        c = Card(rank, suit)
        self.cards.append(c)
        
  def deal(self):
    if len(self) == 0:
      return None
    else:
      return self.cards.pop(0)

  def __str__(self):
    result = ''
    for c in self.cards:
      result = self.result + str(c) + '\n'
    return result

  def shuffle(self):
    random.shuffle(self.cards)

  def __len__(self):
    return len(self.cards)

  

def main():
  deck = Deck()
  print("The following is a new deck\n_________________\n")
  while len(deck) > 0:
    print(deck.deal())
  deck = Deck()
  deck.shuffle()
  print("\n\nThe follwoing is the deck shuffled once \n_______________________________________\n")
  while len(deck) > 0:
    print(deck.deal())

if __name__ == "__main__":
  main()
