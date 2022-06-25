def mostFrequesnt(input):
	frout_list = input.split(' ')
	print(frout_list)

	frouts = {}

	maxFre = 0
	frout = ''
	
	for i in range(len(frout_list)):
		if frout_list[i] not in frouts:
			frouts[frout_list[i]] = 1
		else:
			frouts[frout_list[i]] += 1

		if frouts[frout_list[i]] > maxFre:
			maxFre = max(maxFre, frouts[frout_list[i]])
			frout = frout_list[i]
	print(frouts)

	print(frout, maxFre)


String = "Apple Mango Java Mango Python Apple Mango Html"

print(mostFrequesnt(String))

# {Apple : 1,
# Mango: 3,
# Java : 1,
# Html: 1
#
# #  }
# maxFre = 2
# frout = mango