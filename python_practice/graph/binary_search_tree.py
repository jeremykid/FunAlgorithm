
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
    
