def generateDivTags(numberOfTags):
    # Write your code here.
    divs = []
    def backtrack(open, close, tags, curr_div):
        if tags == 0:
            divs.append(curr_div[:])
            return

        if open == 0 or open == close:
            open_div = backtrack(open+1, close, tags, curr_div + "<div>")
        if 0 < open < numberOfTags and close < open:
            close_div = backtrack(open, close+1, tags-1, curr_div + "</div>")
            open_div = backtrack(open+1, close, tags, curr_div + "<div>")
        elif open == numberOfTags:
            close_div = backtrack(open, close+1, tags-1, curr_div + "</div>")
        return
    backtrack(0, 0, numberOfTags, "")
    return divs

numberOfTags = 3
print(generateDivTags(numberOfTags))