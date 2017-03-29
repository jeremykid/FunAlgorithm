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
	
	def depthFirstSearch(self, start_vertex, finded_vertexes):
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0 and node not in finded_vertexes:
				finded_vertexes.append(node)
				finded_vertexes = self.depthFirstSearch(node, finded_vertexes)
		return finded_vertexes
	

	
	def breathFirstSearch(self, start_vertex, finded_vertexes):
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0 and node not in finded_vertexes:
				finded_vertexes.append(node)
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0 and node not in finded_vertexes:
				finded_vertexes = self.breathFirstSearch(node, finded_vertexes)
		return finded_vertexes
		
	def Dijkstra(self, start):
		#with weight
		distanceList = [float('inf')]*self.degrees
		distanceList[start] = 0
		self.DijkstraRecursion(start, distanceList, [])	
		return distanceList

	def DijkstraRecursion(self ,start ,distance_list ,min_distance_list):
		if len(min_distance_list) == self.degrees:
			return distance_list 
		else:
			min_distance_list.append(start)
			for node in range(self.degrees):
				if self.adjacent_matrix[start][node] != 0:
					new_distance = distance_list[start] + self.adjacent_matrix[start][node]
					if new_distance <= distance_list[node]:
						distance_list[node] = new_distance
			self.DijkstraRecursion(start ,distance_list ,min_distance_list)
		
		
