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
	   	return True

	def depthFirstSeach(self, start_vertex, finded_vertexes):
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0 and node not in finded_vertexes:
				finded_vertexes.append(node)
				finded_vertexes = self.depthFirstSeach(node, finded_vertexes)
		return finded_vertexes
	
	def getAllEdges(self):
		result = []
		for node_start in range(self.degrees):
			for node_end in range(self.degrees):
				if self.adjacent_matrix[node_start][node_end] != 0:
					result.append([node_start, node_end])
		return result
	
	def breathFirstSeach(self, start_vertex, finded_vertexes):
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0 and node not in finded_vertexes:
				finded_vertexes.append(node)
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0 and node not in finded_vertexes:
				finded_vertexes = self.breathFirstSeach(node, finded_vertexes)
		
	def Dijkstra(self, start):
		#with weight
		distanceList = [math.inf]*self.degrees
		distanceList[start] = 0
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0:
				distanceList[node] = distanceList[start] + self.adjacent_matrix[start_vertex][node]
		new_start = distanceList.index(min(distanceList))	
		self.DijkstraRecursion(new_start, distanceList, [start])	
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
		
		
