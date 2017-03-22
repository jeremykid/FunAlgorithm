from undirectedGraph import undirectedGraph

def main():
	test1 = undirectedGraph(6)
	print "==== Empyh Graph ===="
	print test1
	
	test1.addEdge(1,2)
	print "Add edge 1-2"
	print "==== Graph with 1 edge ===="
	print test1
	
	test1.addEdge(1,3)
	test1.addEdge(3,4)
	test1.addEdge(2,5)
	print "==== Graph with 4 edge ===="
	print test1
	
	#todo test depthFirstSearch
	# 1->2
	#    2->5
	# 1->3
	#    3->4
	result = test1.depthFirstSearch(1)
	print "=== Depth First Search ==="
	print result
	
	#todo test breathFirstSearch
	# 1->2
	# 1->3
	#    2->5
	#    3->4
	result = test1.breathFirstSearch(1)
	print "=== Breath First Search ==="
	print result
	
	#todo test get all edges
	result = test1.getAllEdges(1)
	print "=== Get All Edges ==="
	print result
	
	#todo test is tree (is it a cycle)
main()
