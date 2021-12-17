import os
def displayFiles(pathname):
  if (os.path.isdir(pathname)):
    for item in os.listdir(pathname):
      newItem = os.path.join(pathname, item)
      displayFiles(newItem)    
  else:
    filename=pathname
    baseFile = os.path.basename(filename)
    print("File Name: ", baseFile)
    with open(filename, "r") as file:
      print("Content:")
      for line in file:
        print(line)
      print()

def main():
  displayFiles("file1.txt")
  displayFiles("file2.txt")
  directory = os.getcwd()
  print("\n\n\n\n\nContents of the current working directory are listed below: \n")
  displayFiles(directory)
main()
