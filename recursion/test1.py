def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print("k",k,end='')
    print('result',result)
  else:
    result = 0
  return result

tri_recursion(6)