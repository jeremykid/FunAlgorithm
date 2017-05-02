from binary_search_tree import binary_search_tree

def main():
  test1 = binary_search_tree(6)
  print test1
  
  test1.insert_node(7)
  print test1.get_node_count()
  print test1.get_height()
  print test1.get_min()
  print test1.get_max()
  print test1.is_binary_search_tree()
main()
