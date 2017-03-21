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
	
	#todo test breathFirstSearch
	
	#todo test get all edges
	
	#todo test is tree (is it a cycle)
main()
