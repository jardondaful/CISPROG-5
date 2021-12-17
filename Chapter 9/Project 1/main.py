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

  def __eq__(self, other):
    if self is other:
      return True
    elif type(self) != type(other):
      return False
    else:
      return self.name == other.name

  def __lt__(self, other):
    return self.name < other.name

  def __ge__(self, other):
    return self.name >= other.name

def main():
  student1 = Student("Ken", 5)
  student2 = Student("Amy", 5)
  student3 = Student("Ken", 5)
  for i in range(1, 6):
    student1.setScore(i, 98)
    student2.setScore(i, 95)
    student3.setScore(i,98)
  print(student1)
  print("")
  print(student2)
  print("")
  print(student3)
  print("")
  #testing the 'greater than' operation
  print(student1>student2)
  #testing the 'less than' operation
  print(student2<student3)
  #testing the 'equal to' operation
  print(student1==student3)

if __name__ == "__main__":
  main()
