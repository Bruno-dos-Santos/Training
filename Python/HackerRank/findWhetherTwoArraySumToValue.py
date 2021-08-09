#the main goal here is to resolve that O(n) and also to use SETs to improve "in" to O(1) 
def findWhetherTwoArraySumToValue(arryList, value):
  for i in range(0, len(arryList)):
      element = value - arryList[i]
      result = element in arryList
      if result == True:
        return True 
  return False 

print(findWhetherTwoArraySumToValue( [1, 8, 18, -15 , 1], 3)) #should return true
print(findWhetherTwoArraySumToValue( [5], 10))  #should return true
