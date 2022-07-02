def getLowestCommonManager(topManager, reportOne, reportTwo):
    commonManager = None

    def dfs(root):
        nonlocal commonManager

        if not root:
            return 0

        important_report = 0
        for report in root.directReports:
            important_report += dfs(report)
 
        if root(name) == reportOne.name or root(name) == reportTwo.name:
            important_report += 1

        if important_report == 2:
            commonManager = root
            return 0

        return important_report
    dfs(topManager)

    if commonManager != None:
        return commonManager

    return topManager

class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
