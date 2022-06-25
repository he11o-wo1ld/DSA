def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()
	# cur_sum = sum(quries)-quries(len(quries)-1)
	total = 0
	for i, duration in enumerate(queries):
		querieLeft = len(queries) - (i+1)
		total += duration * querieLeft
    return total
