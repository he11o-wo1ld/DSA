def NBitBinary():
	op = ''
	
	def solve(N, op, one, zero, res):
	    if N == 0:
	        res.append(op)
	        return
	    
	    op1 = op
	    op1 = op + '1'
	    solve(N-1, op1, one+1, zero, res)
	    
	    if (one > zero):
	        op2 = op
	        op2 = op2 + '0'
	        solve(N-1, op2, one, zero+1, res)
	N = int(input())
	one = 0
	zero = 0
	res = []
	solve(N, op, one, zero, res)
	return res
	

print(NBitBinary())