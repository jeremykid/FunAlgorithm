def bubble_sort(input_list):
  input_list_length = len(input_list)
  for passed in range(input_list_length-1):
    for index in range(input_list_length-1):
      if (input_list[index] > input_list[index+1]):
        input_list[index], input_list[index+1] =  input_list[index+1], input_list[index]
      # print input_list
  return input_list
  
def insert_sort(input_list):
  input_list_length = len(input_list)
  for i in range(1,input_list_length):
    result_list = insert_sort_single_sort(input_list[:i], input_list[i])
    if (i != input_list_length):
      input_list = result_list + input_list[i+1:] 
  return input_list

def insert_sort_single_sort(input_list, new_element):
  is_insert = False
  for i in range(len(input_list)):
    if input_list[i] > new_element:
      input_list.insert(i,new_element)
      is_insert = True
  if is_insert == False:
    input_list.append(new_element)
  return input_list

def merge_sort(input_list):
  input_list_length = len(input_list)
  result_list = input_list
  if (input_list_length > 1):
    mid = input_list_length//2
    left_list = input_list[:mid]
    right_list = input_list[mid:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    
    left_index = 0
    right_index = 0
    index = 0
    result_list = [0]*input_list_length
    while left_index < len(left_list) and right_index < len(right_list):
      if left_list[left_index] < right_list[right_index]:
        result_list[index] = left_list[left_index]  
        left_index = left_index+1
      else:
        result_list[index] = right_list[right_index]  
        right_index = right_index+1
      index += 1 

    while left_index < len(left_list):
      result_list[index] = left_list[left_index]  
      left_index = left_index+1
      index += 1 

    while right_index < len(right_list):
      result_list[index] = right_list[right_index]  
      right_index = right_index+1
      index += 1 
  return result_list
        
def quick_sort(input_list):
  input_list_length = len(input_list)
  if input_list_length <= 1:
    return input_list
  mark = input_list[0]
  less_list = []
  more_list = []
  for i in range(1, input_list_length):
    if (input_list[i] > mark):
      more_list.append(input_list[i])
    else:
      less_list.append(input_list[i])
  return qsort(less_list) + [mark] + qsort(more_list)
