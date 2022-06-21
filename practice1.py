#prints out a new sorted array without any duplicate elements
x = [4,3,2,1,1,2,6]
print ("The original list is : " +  str(x))
  
y = []
def remove_duplicates(x):
  for i in x:
      if i not in y:
          y.append(i)
  y.sort()
  print ("List after removing duplicates : " + str(y))


remove_duplicates(x) 
