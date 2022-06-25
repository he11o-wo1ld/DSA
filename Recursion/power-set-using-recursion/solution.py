def powerset(array):
    op = []
    res = []

    def solve(ip, op, res):
        if len(ip) == 0:
            res.append(op)
            return

        op1 = op
        op2 = op

        op2.append(ip[0])
        ip = ip[1:]

        solve(ip, op1, res)
        solve(ip, op2, res)

        return res

    solve(array, op, res)
    return res

arr = [1,2,3]
print(powerset(arr))
