
class binary_search_tree(object):
  def __init__(self, value):
    self.value = value
    self.right_node = None
    self.left_node = None

  def __str__(self):
    print self.left_node
    print self.value
    print self.right_node

  def insert_node(self, insert_value):
    if insert_value == self.value:
      return false
    if insert_value > self.value:
      if self.right_node == None:
        self.right_node = binary_search_tree(insert_value)
      else:
        self.right_node.insert_node(insert_value)
    else:
      if self.left_node == None:
        self.left_node = binary_search_tree(insert_value)
      else:
        self.left_node.insert_node(insert_value)
    return true
  
  def get_node_count(self):
    return_count = 1
    if self.right_node != None:
      return_count += self.right_node.get_node_count()
    if self.left_node != None:
      return_count += self.left_node.get_node_count()
    return return_count
  
  def get_height(self):
    return_height = 1
    return_right_height = 0
    return_left_height = 0
    if self.right_node != None:
      return_right_height += self.right_node.get_height()
    if self.left_node != None:
      return_left_height += self.left_node.get_height()
    return_height += max(return_right_height,return_left_height)
  
  def get_min(self):
    if self.left_node == None:
      return self.value
    else:
      return self.left_node.get_min()
    
  def get_max(self):
    if self.right_node == None:
      return self.value
    else:
      return self.right_node.get_max()
    
  def is_binary_search_tree(self):
    result = false
    if self.left_node.value < self.left_node.get_max():
      return result
    else:
      result = (result and self.left_node.is_binary_search_tree())
    if self.right_node.value > self.right_node.get_min():
      return result
    else:
      result = (result and self.left_node.is_binary_search_tree())
    return result
  
  def is_in_tree(self):
    #todo
    return true
