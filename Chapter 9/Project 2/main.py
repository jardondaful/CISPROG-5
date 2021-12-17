import random
class Student(object):
  def __init__(self, name, number):
    self.name = name
    self.scores = []
    for count in range(number):
      self.scores.append(0)

  def getName(self):
    return self.name

  def setScore(self, i, score):
    self.scores[i - 1] = score

  def getScore(self, i):
    return self.scores[i - 1]

  def getAverage(self):
    return sum(self.scores) / len(self._scores)

  def getHighScore(self):
    return max(self.scores)

  def __str__(self):
    return "Name: " + self.name + "\nScores: " + \
" ".join(map(str, self.scores))

  def __lt__(self, other):
    return self.name < other.name

  def __ge__(self, other):
    return self.name >= other.name

  def __eq__(self, other):
    if self is other:
      return True
    elif type(self) != type(other):
      return False
    else:
      return self.name == other.name

def main():
  lyst = []
  student1 = Student("Amy", 10)
  student2 = Student("Bob", 10)
  student3 = Student("Kelly", 10)
  student4 = Student("Jordan", 10)
  student5 = Student("Nancy", 10)
  lyst.append(student1)
  lyst.append(student2)
  lyst.append(student3)
  lyst.append(student4)
  lyst.append(student5)
  for i in range(10):
    student1.setScore(i, 98)
  for i in range(10):
    student2.setScore(i, 87)
  for i in range(10):
    student3.setScore(i, 91)
  for i in range(10):
    student4.setScore(i, 76)
  for i in range(10):
    student5.setScore(i, 82)
  random.shuffle(lyst)
  print("Content of Unsorted List of Students " + "\n"+ "_______________________________________" + "\n")
  for s in lyst:
    print(s)
    print("")
  lyst.sort()
  print("\nSorted Content of List of Students (in descending order) " + "\n"+ "_________________________________________________________" + "\n")
  for s in lyst:
    print(s)
    print("")

if __name__ == "__main__":
  main()
