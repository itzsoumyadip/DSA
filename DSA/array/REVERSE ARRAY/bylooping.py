# code  start from here 
def reverse(array):
  new_array=[]
  for a in range(len(array)-1,0,-1):
    new_array.append(array[a])

  return new_array


arr=reverse([23,42,42,53,23,54])
print(arr)

