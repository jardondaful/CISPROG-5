def is_sorted(a_list):
  for i in range(len(a_list)-1):
    if a_list[i+1]<a_list[i]:
      return False
  return True

def main():
  print(is_sorted([1,2,3]))
  print(is_sorted([3,2,1]))

main()
