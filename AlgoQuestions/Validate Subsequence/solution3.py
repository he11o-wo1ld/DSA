def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIdx = 0
	for i in array:
		if seqIdx == len(sequence):
			return True
		if sequence[seqIdx] == i:
			seqIdx += 1
	return seqIdx == len(sequence)
