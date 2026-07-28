graph = {}
h = {}

n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("\nEnter node: ")
    
    value = int(input(f"Enter heuristics of {node}: "))
    h[node] = value
    
    neighbours = input(f"Enter neighbours of {node}: ").split()
    weights = input("Enter edge costs: ").split()
    
    graph[node] = {}
    for neighbour, weight in zip(neighbours, weights):
        graph[node][neighbour] = int(weight)
    
start = input("\nEnter the start node: ")
goal = input("Enter the goal state: ")


def OccursIn(node, nodeList):
    for item in nodeList:
        if item[0] == node:
            return True
    return False


def GetItem(node, nodeList):
    for item in nodeList:
        if item[0] == node:
            return item
    return None


def ReconstructPath(item, closed):
    path = [item[0]]
    parent = item[1]
    
    while parent is not None:
        path.insert(0, parent)
        
        for elem in closed:
            if elem[0] == parent:
                item = elem
                break
        
        parent = item[1]
        
    return path


def PropagateImprovement(node, closed):
    neighbours = graph[node]
    M = GetItem(node, closed)
    
    for neighbour in neighbours:
        S = GetItem(neighbour, closed)
        
        if S is not None:
            newG = M[2] + graph[node][neighbour]
            
            if newG < S[2]:
                S[1] = node
                S[2] = newG
                S[4] = newG + h[neighbour]
                
                if OccursIn(neighbour, closed):
                    PropagateImprovement(neighbour, closed)
    

def AStar():
    open = [[start, None, 0, h[start], h[start]]]
    closed = []
    
    while open:
        open.sort(key=lambda x: (x[4], x[3]))
        
        print("\nOPEN:        ", open)
        print("CLOSED:      ", closed)
        
        item = open.pop(0)
        node = item[0]
        
        if node == goal:
            print("\nGoal found")
            print("Solution path: ", " -> ".join(ReconstructPath(item, closed)))
            return
        
        closed.insert(0, item)
        
        neighbours = graph[node]
        
        for neighbour in neighbours:
            newG = item[2] + graph[node][neighbour]
            newF = newG + h[neighbour]
            
            if not OccursIn(neighbour, open) and not OccursIn(neighbour, closed):
                newNode = [neighbour, node, newG, h[neighbour], newF]
                open.append(newNode)
            elif OccursIn(neighbour, open):
                M = GetItem(neighbour, open)
                if newG < M[2]:
                    M[1] = node
                    M[2] = newG
                    M[4] = newF
            elif OccursIn(neighbour, closed):
                M = GetItem(neighbour, closed)
                if newG < M[2]:
                    M[1] = node
                    M[2] = newG
                    M[4] = newF
                    PropagateImprovement(neighbour, closed)
    
    return "No solution found"
              
                    
AStar()