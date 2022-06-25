def taskAssignment(k, tasks):
	pairedTask = []
    taskDurationToIndices = getTaskDurationToIndices(tasks)

    sortedTasks = sorted(tasks)

    for idx in range(k):
		task1Duration = sortedTasks[idx]
		indicesWithTask1Duration = taskDurationToIndices[task1Duration]
		task1Index = indicesWithTask1Duration.pop()
		
		task2SortedIndex = len(tasks) - 1 - idx
		
		task2Duration = sortedTasks[task2SortedIndex]
		indicesWithTask2Duration = taskDurationToIndices[task2Duration]
		task2Index = indicesWithTask2Duration.pop()
		
		pairedTask.append([task1Index, task2Index])
	return pairedTask


def getTaskDurationToIndices(tasks):
    taskDurationToIndices = {}
    for idx, value in enumerate(tasks):
        if value in taskDurationToIndices:
            taskDurationToIndices[value].append(idx)
        else:
            taskDurationToIndices[value] = [idx]
    return taskDurationToIndices
 