def generateParenthesis(A):
    res = []

    def solve(Open, Close, op, res):
        if Open == 0 and Close == 0:
            res.append(op)
            return res

        if Open != 0:
            op1 = op
            op1 = op1 + '('
            solve(Open-1, Close, op1, res)
        
        if Close > Open:
            op2 = op
            op2 = op2 + ')'
            solve(Open, Close-1, op2, res)

    Open = A
    Close = A
    op = ''
    solve(Open, Close, op, res)
    return res
    
print(generateParenthesis(5))