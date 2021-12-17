def myRange(*parameters):
  myList=[]
  if len(parameters) is 1:
    k=0
    if parameters[0] > 0:
      while k < parameters[0]:
          myList.append(k)
          k=k+1
    else:
      while k > parameters[0]:
        myList.append(k)
        k=k-1
  elif len(parameters) is 2:
    k = parameters[0]
    if parameters[0] < parameters[1]:
      while k < parameters[1]:
        myList.append(k)
        k=k+1
    else:
      while k > parameters[1]:
        myList.append(k)
        k=k-1
  else:
    k=parameters[0]
    if parameters[0] < parameters[1]:
      while k < parameters[1]:
        myList.append(k)
        k=k+parameters[2]
    else:
      while k > parameters[1]:
        myList.append(k)
        k=k+parameters[2]
  return myList

def main():
  print(myRange(10), "\n")
  print(myRange(-10), "\n")
  print(myRange(10,20), "\n")
  print(myRange(10,-10), "\n")
  print(myRange(10,10), "\n") #same parameters
  print(myRange(2,25,3), "\n")
  print(myRange(25,2,-3), "\n")

main()
