
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
  
  
