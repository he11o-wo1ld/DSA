def mergeOverlappingIntervals(interval):
	sortedInterval = sorted(interval, key=lambda x: x[0])

	mergedInterval = []
	currentInterval = sortedInterval[0]
	mergedInterval.append(currentInterval)

	for nextInterval in sortedInterval:
		_, currentIntervalEnd = currentInterval
		nextIntervalStart, nextIntervalEnd = nextInterval

		if currentIntervalEnd >= nextIntervalStart:
			currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)

		else:
			currentInterval = nextInterval
			mergedInterval.append(currentInterval)
	return mergedInterval
