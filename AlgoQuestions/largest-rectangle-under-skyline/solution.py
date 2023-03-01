def largestRectangleUnderSkyline(A):
    # Write your code here.
    def f(b, e):
        if b == e:
            return 0

        m = b
        for i in range(b, e):
            if A[i] < A[m]:
                m = i
        return max(A[m] * (e - b), f(b, m), f(m + 1, e))
    return f(0, len(A))
    
A = [1, 3, 3, 2, 4, 1, 5, 3, 2]
print(largestRectangleUnderSkyline(A))
