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

	def addEdge(self, vertex1, vertex2):
		self.adjacent_matrix[vertex1][vertex2]+=1
		self.adjacent_matrix[vertex2][vertex1]+=1

        def isTree(self):
	   	return True

	def depthFirstSeach(self, start_vertex, finded_vertexes):
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0 and node not in finded_vertexes:
				finded_vertexes.append(node)
				finded_vertexes = self.depthFirstSeach(self, start_node, finded_vertexes)
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
			finded_vertexes = self.breathFirstSeach(self, start_node, finded_vertexes)
		
	def Dijkstra(self, start, end):
		#with weight
		distanceList = [math.inf]*self.degrees
		distanceList[start] = 0
		for node in range(self.degrees):
			if self.adjacent_matrix[start_vertex][node] != 0:
						
		return [];
