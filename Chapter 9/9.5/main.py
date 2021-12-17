import random
class Doctor(object):
  history = []
  hedges = ("Please tell me more.",
  "Many of my patients tell me the same thing.",
  "Please coninue.")
  qualifiers = ("Why do you say that ",
  "You seem to think that ",
  "Can you explain why ")
  replacements = {"I": "you", "me": "you", "my": "your",
  "we": "you", "us": "you", "mine": "yours",
  "you": "I", "your": "my", "yours": "mine"}

  def __init__(self):
    pass

  def reply(self, sentence):
    probability = random.randint(1, 5)
    if probability in (1, 2):
      answer = random.choice(Doctor.hedges)
    elif probability == 3 and len(Doctor.history) > 3:
      answer = "Earlier you said that " + \
      self.changePerson(random.choice(Doctor.history))
    else:
      answer = random.choice(Doctor.qualifiers) + \
      self.changePerson(sentence)
    Doctor.history.append(sentence)
    return answer
    
  def changePerson(self, sentence):
    words = sentence.split()
    replyWords = []
    for word in words:
      replyWords.append(Doctor.replacements.get(word, word))
    return " ".join(replyWords)

  def greeting(self):
    return "Hi, Let's get started"
  def farewell(self):
    return "Time's up, Let's pick up here next week"

def main():
  d = Doctor()
  print(d.greeting())
  while True:
    sentence = input("\n>> ")
    if sentence.upper() == "QUIT":
      print(d.farewell())
      break
    print(d.reply(sentence))

if __name__ == "__main__":
  main()
