def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	
	if not fastest:
		reverseArrayInPlace(redShirtSpeeds)
	
	total = 0
	for i in range(len(blueShirtSpeeds)):
		rider1 = redShirtSpeeds[i]
		rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - i -1]
		total += max(rider1, rider2)
		
    return total

def reverseArrayInPlace(arr):
	start = 0
	end = len(arr) - 1
	while start < end:
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1