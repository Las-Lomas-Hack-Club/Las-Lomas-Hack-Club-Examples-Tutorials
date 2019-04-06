#quick example on how to use lists and 'in' keyword
def has99(nums):
  list_num = 0
  for num in nums:
    list_num += 1
    if (nums[list_num] == 9) and(nums[list_num + 1 ] == 9):
      print('true')
      return True
    else:
      print('false')
      return False
has99([1,2,3,3,6,7,8,9,9])
