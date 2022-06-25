# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    depthOne = getDepth(descendantOne, topAncestor)
	depthTwo = getDepth(descendantTwo, topAncestor)
	
	if depthOne > depthTwo:
		return getCommonAnscestor(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return getCommonAnscestor(descendantTwo, descendantOne, depthTwo - depthOne)
	
def getDepth(descendant, topAncestor):
	depth = 0
	while descendant != topAncestor:
		descendant = descendant.ancestor
		depth += 1
	return depth

def getCommonAnscestor(lowerDescendant, upperDescendant, depth):
	while depth > 0:
		lowerDescendant = lowerDescendant.ancestor
		depth -= 1
	
	while lowerDescendant != upperDescendant:
		lowerDescendant = lowerDescendant.ancestor
		upperDescendant = upperDescendant.ancestor
	return upperDescendant
	
	
	

	
# Context
import program
import unittest


class AncestralTree(program.AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"])
        trees["B"].addDescendants(trees["D"], trees["E"])
        trees["D"].addDescendants(trees["H"], trees["I"])
        trees["C"].addDescendants(trees["F"], trees["G"])

        yca = program.getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
        self.assertTrue(yca == trees["B"])
