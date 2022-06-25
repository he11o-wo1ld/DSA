def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
	if len(blueShirtHeights) != len(redShirtHeights):
		return False
	
	blueShirtHeights.sort(reverse=True)
	redShirtHeights.sort(reverse=True)
	
	color = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
	
	for i in range(len(redShirtHeights)):
		r_height = redShirtHeights[i]
		b_height = blueShirtHeights[i]
		
		if color == "RED":
			if r_height >= b_height:
				return False
		else:
			if b_height >= r_height:
				return False
	return True
