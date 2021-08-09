# pass a word and a string and the app gives you the diff between the leftmost and the rigtmost of that word 
def programmerStrings(word, strInput):
  start = 0
  end = len(strInput)-1
  letters = [letter for letter in word]
  while (start < len(strInput) and len(letters) > 0):
    if strInput[start] in letters: 
      letters.remove(strInput[start])
    start = start + 1
    
  letters = [letter for letter in word]

  while (end >= 0 and len(letters)>0):
    if strInput[end] in letters: 
      letters.remove(strInput[end])
    end = end - 1

  if (start > end ): return -1 
  return end - start + 1

print(programmerStrings("programmer", "progxrammerrxproxgrammer"))  
