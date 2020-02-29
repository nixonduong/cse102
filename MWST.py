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
    for edge in splitFile[2:]:
        x, y, z = edge.split()
        E.append((int(x), int(y)))
        w[(int(x), int(y))] = float(z)
    fileHandler.close()
    return ((V, E, w))

def test(problem, output_file):
    fileHandler = open(output_file, 'w')
    fileHandler.write(str(len(problem[0])) + '\n')
    fileHandler.write(str(len(problem[1])) + '\n')
    for x, y in problem[1]:
        fileHandler.write(str(x) + ' ' + str(y) + ' ' + str(int(problem[2][(x, y)])) + '\n')
    fileHandler.close()

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    problem = createInstanceOfProblem(input_file)
    test(problem, output_file)

if __name__ == '__main__':
    main()