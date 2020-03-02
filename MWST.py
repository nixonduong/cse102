# Student: Nixon Duong
# CruzID: niduong
# Professor: Patrick Tantalo
# Course: CMPS102
# Programming Assignment: PA1
# Description: Given a connected weighted graph G through an input_file,
#              outputs a minimum weight spanning tree of G to output_file 
# File: MWST.py
import sys

# Input: string: input_file
# Output: WG (int[]: V, int[]: E, <int:key, float:val>{}: w)
def createInstanceOfProblem(input_file):
    fileHandler = open(input_file, 'r')
    splitFile = fileHandler.readlines()
    n = int(splitFile[0])
    V = [i for i in range(1, n + 1)]
    E = []
    w = {}
    labels = {}
    i = 1
    for edge in splitFile[2:]:
        try:
            x, y, z = edge.split()
        except:
            pass
        E.append((int(x), int(y)))
        w[(int(x), int(y))] = float(z)
        labels[(int(x), int(y))] = i
        i += 1
    fileHandler.close()
    return (((V, E, w), labels))

def findSet(x, disjointSet):
    i = 0
    index = None
    for i in range(len(disjointSet)):
        if x in disjointSet[i]:
            index = i
            break
    return index

# Input: (V, E, w): problem
# Output: (V, E, w): minimumSpanningTree
def getMinimumSpanningTree(problem):
    # Decompose problem into vertex set, edge set and weight function
    V = problem[0]
    E = problem[1]
    w = problem[2]
    # Sort all edges in accending weight
    E = sorted(E, key=lambda edge: w[edge])
    # Initialization
    disjointSet = [set([v]) for v in V]
    # Kruskal's Algorithm
    F = []
    for x, y in E:
        if len(disjointSet[findSet(x, disjointSet)].difference(disjointSet[findSet(y, disjointSet)])) > 0:
            F.append((x, y))
            setY = disjointSet[findSet(y, disjointSet)]
            disjointSet.pop(findSet(y, disjointSet))
            disjointSet[findSet(x, disjointSet)] = disjointSet[findSet(x, disjointSet)].union(setY)
        if len(F) == len(V) - 1:
            break
    # return minimum spanning tree of problem
    return ((V, F, w))

# Input: (V, E, W): solution, str: output_file, <(int:x, int:y), int:label>{}: labels
# Output: void
def writeSolutionToFile(solution, output_file, labels):
    fileHandler = open(output_file, 'w')
    totalWeight = 0
    for edge in solution[1]:
        fileHandler.write('{:>4}: {} {:.1f}\n'.format(labels[edge], edge, solution[2][edge]))
        totalWeight += solution[2][edge]
    fileHandler.write('Total Weight = {:.2f}'.format(totalWeight))
    fileHandler.close()

# Input: void
# Output: void
def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    problem, labels = createInstanceOfProblem(input_file)
    solution = getMinimumSpanningTree(problem)
    writeSolutionToFile(solution, output_file, labels)

if __name__ == '__main__':
    main()