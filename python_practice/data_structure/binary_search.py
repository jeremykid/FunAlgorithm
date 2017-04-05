
def binarySearchList(space_list, target):
  space_list.sort()
  space_list_length = len(space_list)
  lo = 0
  hi = space_list_length
  while lo < hi:
    mid = (lo+hi)//2
    if space_list[mid] == target:
      return mid
    else if space_list[mid] > target:
      hi = mid-1
    else:
      lo = mid+1
  if space_list[lo] == target:
    return lo
  return -1
