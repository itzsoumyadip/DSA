def max(array):
  arr=array[0]
  for i in range (len(array)-1):
    if array[i]>arr:
      arr,array[i]=array[i],arr
  return arr

def min(array):
  arr=array[0]
  for i in range (len(array)-1):
    if array[i]<arr:
      arr,array[i]=array[i],arr
  return arr


a=max([23,54,64,21,564,64,344])
print(a)    
b=min([23,54,64,21,564,64,344])
print(b)    

