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
        x, y, z = edge.split()
        E.append((int(x), int(y)))
        w[(int(x), int(y))] = float(z)
        labels[(int(x), int(y))] = i
        i += 1
    fileHandler.close()
    return (((V, E, w), labels))

# Input: int: x, int: y, set[]: disjointSet, int[]: findSet
# Output: set[]: disjointSet, int[]: findSet
def union(x, y, disjointSet, findSet):
    disjointSet[findSet[x]] = disjointSet[findSet[x]]|disjointSet[findSet[y]]
    findSet[y] = findSet[x]
    return ((disjointSet, findSet))

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
    findSet = {}
    i = 0
    for v in V:
        findSet[v] = i
        i += 1
    vertexSet = {v for v in V}
    # Kruskal's Algorithm
    F = []
    for x, y in E:
        if not disjointSet[findSet[x]] == disjointSet[findSet[y]]:
            F.append((x, y))
            disjointSet, findSet = union(x, y, disjointSet, findSet)
        if vertexSet in disjointSet:
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