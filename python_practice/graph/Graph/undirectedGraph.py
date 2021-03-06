import math


class undirectedGraph(object):
	def __init__(self, degrees):
		self.degrees = degrees
		self.adjacent_matrix = []
		for i in range(degrees):
			self.adjacent_matrix.append([0]*degrees)

	def __str__(self):
		output = ""
		for row in self.adjacent_matrix:
			for item in row:
				output += "|"+str(item)
			output += "|\n"
		return output

	def addEdge(self, vertex1, vertex2, weight = 1):
		if (vertex1 >= self.degrees or vertex2 >= self.degrees):
			print ("index out of range")
		else:
			self.adjacent_matrix[vertex1][vertex2] += weight
			self.adjacent_matrix[vertex2][vertex1] += weight

        def isTree(self):
		#copy the adjacent matrix 
		#let used edge = 0
		for row in range(self.degrees):
			for node in range(self.degrees):
				#use depthFirstSeach to check if there are back
				break
	   	return True

	def getAllEdges(self):
		result = []
		for node_start in range(self.degrees):
			for node_end in range(self.degrees):
				if self.adjacent_matrix[node_start][node_end] != 0:
					result.append([node_start, node_end])
		return result
	
	# def getAllWeight(self):
	# 	allEdgeList = self.getAllEdges()
	# 	result = {}
	# 	for i in allEdgeList:
	# 		print (self.adjacent_matrix[i[0]][i[1]])
	# 		result[i] = self.adjacent_matrix[i[0]][i[1]]
		
	# 	return result
		
	def getOneMiniWeight(self, temp_adjacent_matrix = []):
		if temp_adjacent_matrix == []:
			temp_adjacent_matrix = self.adjacent_matrix
		
		min_weight = float('inf')
		for row in range(self.degrees):
			for col in range(self.degrees):
				if (temp_adjacent_matrix[row][col] != 0 and temp_adjacent_matrix[row][col] < min_weight):
					min_weight = temp_adjacent_matrix[row][col]
					min_row = row
					min_col = col
		return [min_row, min_col, min_weight]
	
	def depthFirstSearch(self, start_vertex, finded_vertexes):
		if (start_vertex >= self.degrees):
			return "Index out of range"
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0 and node not in finded_vertexes:
				finded_vertexes.append(node)
				finded_vertexes = self.depthFirstSearch(node, finded_vertexes)
		return finded_vertexes
	

	
	def breathFirstSearch(self, start_vertex, finded_vertexes):
		if (start_vertex >= self.degrees):
			return "Index out of range"
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0 and node not in finded_vertexes:
				finded_vertexes.append(node)
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0 and node not in finded_vertexes:
				finded_vertexes = self.breathFirstSearch(node, finded_vertexes)
		return finded_vertexes
		
	def Dijkstra(self, start):
		if (start >= self.degrees):
			return "Index out of range"
		#with weight
		distanceList = [float('inf')]*self.degrees
		distanceList[start] = 0
		min_distance_list = [0]*self.degrees
		min_distance_list[start] = 1
		self.DijkstraRecursion(start, distanceList, min_distance_list)	
		return distanceList

	def DijkstraRecursion(self ,start ,distance_list ,min_distance_list):
		if sum(min_distance_list) == self.degrees:
			return distance_list 
		else:
			for node in range(self.degrees):
				if self.adjacent_matrix[start][node] != 0:
					new_distance = distance_list[start] + self.adjacent_matrix[start][node]
					if new_distance <= distance_list[node]:
						distance_list[node] = new_distance
			#start = min(min_distance_list)
			temp_min_distance_list = list(min_distance_list)
			temp_min_distance_list.sort()
			start = min_distance_list.index(temp_min_distance_list[0])
			min_distance_list[start] = 1
			self.DijkstraRecursion(start ,distance_list ,min_distance_list)
		
	def minimum_spanning_tree(self):
		result_adjacent_matrix = []
		for i in range(self.degrees):
			result_adjacent_matrix.append([0]*self.degrees)
		# edges_weight = self.getAllWeight()
		linked_vertexs = [0]*self.degrees
		changed_adjacent_matrix = [x[:] for x in self.adjacent_matrix]
		result_adjacent_matrix = self.minimum_spanning_tree_recursion(result_adjacent_matrix, linked_vertexs, changed_adjacent_matrix)
		return result_adjacent_matrix

	def minimum_spanning_tree_recursion(self, result_adjacent_matrix, linked_vertexs, changed_adjacent_matrix):
		if sum(linked_vertexs) == 2*self.degrees - 2:
		    	return  result_adjacent_matrix
		else: 
			min_edge = self.getOneMiniWeight(changed_adjacent_matrix)
			if min_edge[2] = float("inf"):
				return result_adjacent_matrix
			
			if linked_vertexs[min_edge[0]] <= 1 and linked_vertexs[min_edge[1]] <= 1: 
				result_adjacent_matrix[min_edge[0]][min_edge[1]] = min_edge[2]
				result_adjacent_matrix[min_edge[1]][min_edge[0]] = min_edge[2]
				changed_adjacent_matrix[min_edge[0]][min_edge[1]] = 0
				changed_adjacent_matrix[min_edge[1]][min_edge[0]] = 0
				linked_vertexs[min_edge[0]] += 1
				linked_vertexs[min_edge[1]] += 1
			else:
				changed_adjacent_matrix[min_edge[0]][min_edge[1]] = 0
				changed_adjacent_matrix[min_edge[1]][min_edge[0]] = 0
				
			self.minimum_spanning_tree_recursion(result_adjacent_matrix, linked_vertexs, changed_adjacent_matrix)
	
	def travelling_salesman_problem(self):
		#Asking
		return 0
