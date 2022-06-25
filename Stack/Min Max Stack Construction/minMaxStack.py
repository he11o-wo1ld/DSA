class MinMaxStack:
    def __init__(self):
        self.MinMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.MinMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {'min': number, "max": number}
        if len(self.MinMaxStack):
            lastMinMax = self.MinMaxStack[len(self.MinMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)

        self.MinMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.MinMaxStack[len(self.MinMaxStack) - 1]["min"]

    def getMax(self):
        return self.MinMaxStack[len(self.MinMaxStack) - 1]["max"]