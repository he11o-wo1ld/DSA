def twoColorable(edges):
    # Write your code here.
    colors = [None] * len(edges)

    for v in range(len(edges)):
        if colors[v] == None:
            colors[v] = True

        for n in edges[v]:
            if colors[n] != None and colors[n] == colors[v]:
                return False
            colors[n] = not colors[v]
    return True

edges = [
    [1, 4],
    [0, 2, 3],
    [1, 3, 4],
    [1, 2],
    [0, 2]
    ]

print(twoColorable(edges))
