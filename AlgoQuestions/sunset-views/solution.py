def sunsetViews(buildings, direction):
    res = []
    stack = []

    if direction == 'EAST':
        for i in range(len(buildings)-1, -1, -1):
            stack.append(buildings[i])
    else:
        for i in range(len(buildings)):
            stack.append(buildings[i])
    return stack


buildings = [3, 5, 4, 4, 3, 1, 3, 2],
direction =  "EAST"
print(sunsetViews(buildings, direction))

print(ord('?'))