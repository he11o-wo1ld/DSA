WHITE, GREY, BLACK = 0, 1, 2
def cycleInGraph(edges):
	numberOfNodes = len(edges)
	color = [WHITE for _ in range(numberOfNodes)]
	
	for node in range(numberOfNodes):
		if color[node] != WHITE:
			continue
		
		countCycle = findColorNode(node, color, edges)
		
		if countCycle:
			return True
	return False

def findColorNode(node, color, edges):
	color[node] = GREY
	neighbors = edges[node]
	
	for neighbor in neighbors:
		neighborColor = color[neighbor]
		
		if neighborColor == GREY:
			return True
		
		if neighborColor != WHITE:
			continue
		
		containCycle = findColorNode(neighbor, color, edges)
		
		if containCycle:
			return True
	color[node] = BLACK
	return False
