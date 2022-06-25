def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    if width is 1 or height is 1:
		return 1
	return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)
