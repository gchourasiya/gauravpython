#Write a method to give the character which is repeating consecutively maximum number of times

check_string ='aabbbbcccddddddeeeeeeeefffgghhhha'


def maxRepeating(str):
  l = len(str)
  count = 0

  # Find the maximum repeating
  # character starting from str[i]
  res = str[0]
  for i in range(l):

    cur_count = 1
    for j in range(i + 1, l):

      if (str[i] != str[j]):
        break
      cur_count += 1

    # Update result if required
    if cur_count > count:
      count = cur_count
      res = str[i]
  return res,count

print(maxRepeating(check_string))