
def binary_search(target, numbs,pointer=0):
  if len(numbs) == 1:
    print("trigger")
    if pointer == target:
      return pointer
    
    return
    #else:
      #return None  
      

  mid = int(len(numbs)/2)
  print(mid)
  if target < numbs[mid]:
    numbs = numbs[:mid]
    print("left side!")
    pointer = binary_search(target,numbs,pointer) 
    return pointer
  elif target == numbs[mid]:
    print(pointer)
    pointer += mid 
    print("found")
    return pointer
    
  else: #target > numbs[mid]:
    numbs = numbs[mid:]
    pointer += mid
    print(numbs)
    print("right side!")
    pointer = binary_search(target,numbs,pointer) 
    return pointer
def main():
    nums = [1,2,3,4,5,6,7,8,9]

    test1 = binary_search(2, nums)
    print("\n\nTest 1 - search for 2")
    print(f"Your returned index: {test1}")
    print(f"Test passed? {test1 == 1}\n\n")

    test2 = binary_search(7, nums)
    print("Test 2 - search for 7")
    print(f"Your returned index: {test2}")
    print(f"Test passed? {test2 == 6}\n\n")

    test3 = binary_search(9, nums)
    print("Test 3 - search for 9")
    print(f"Your returned index: {test3}")
    print(f"Test passed? {test3 == 8}\n\n")
    
    test4 = binary_search(99, nums)
    print("Test 4 - number doesn't exist")
    print(f"Your returned index: {test4}")
    print(f"Test passed? {test4 == None}\n\n")

if __name__ == "__main__":
    main()