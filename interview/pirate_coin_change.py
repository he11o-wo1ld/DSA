def coinDistribution(coin, pirates):
	start = 65
	end = 91
	res = {}
	
	most = coin - (pirates-1) // 2
	
	for i in range(pirates):
		char = chr(start + i)
		if char == 'A':
			res[char] = most
		elif char == 'B':
			res[char] = 0
		else:
			if i % 2 == 0:
				res[char] = 1
			else:
				res[char] = 0
	return res
	
	
pirates = 7
coin = 100
print(coinDistribution(coin, pirates))
