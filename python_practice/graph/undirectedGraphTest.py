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
	result = test1.depthFirstSearch(1,[])
	print "=== Depth First Search ==="
	print result
	
	#todo test breathFirstSearch
	# 1->2
	# 1->3
	#    2->5
	#    3->4
	result = test1.breathFirstSearch(1,[])
	print "=== Breath First Search ==="
	print result
	
	#todo test get all edges
	result = test1.getAllEdges()
	print "=== Get All Edges ==="
	print result
	
	result = test1.Dijkstra(1)
	print "=== Dijkstra ==="
	print result
	#todo test is tree (is it a cycle)

	test2 = undirectedGraph(6)
	#0->1
	#0->4
	#1->2
	#1->3
	#3->5
	#2->5
	#4->5
	test2.addEdge(0,1)
	test2.addEdge(0,4)
	test2.addEdge(1,2)
	test2.addEdge(1,3)
	test2.addEdge(3,5)
	test2.addEdge(2,5)
	test2.addEdge(4,5)
	print "==== 2nd Graph with 7 edges ===="
	print test2
	
	test3 = undirectedGraph(6)
	#0->1 2
	#0->4 4
	#1->2 5
	#1->3 6
	#3->5 2
	#2->5 1
	#4->5 7
	test3.addEdge(0,1,2)
	test3.addEdge(0,4,4)
	test3.addEdge(1,2,5)
	test3.addEdge(1,3,6)
	test3.addEdge(3,5,2)
	test3.addEdge(2,5,1)
	test3.addEdge(4,5,7)
	print "==== 3rd weight Graph with 7 edges ===="
	print test3

	print "==== 3rd weight Graph with get All Weight() ===="
	result = test3.getAllWeight():

main()
