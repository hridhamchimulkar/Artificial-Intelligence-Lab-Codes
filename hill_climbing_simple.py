graph = {}
h = {}

n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("\nEnter node: ")
    value = int(input(f"Enter heuristics of {node}: "))
    h[node] = value
    neighbours = input(f"Enter neighbours of {node}: ").split()
    graph[node] = neighbours
    
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")


def HillClimbing():
    node = start
    parent = None
    path = [node]
    
    while True:
        if node == goal:
            print("\nGoal found")
            break
        
        print("\nNode:         ", (node, parent, h[node]))
        
        neighbours = graph[node]
        
        print("Neighbours: ", end="")
        
        if not neighbours:
            print("\nNo solution found")
            break
        
        for neighbour in neighbours:
            print((neighbour, node, h[neighbour]), end=" ")
        print()
            
        newNode = None
        plateau = False
        
        for neighbour in neighbours:
            if h[neighbour] < h[node]:
                newNode = neighbour
                break  
            elif h[neighbour] == h[node]:
                plateau = True

        if newNode:
            parent = node
            node = newNode
            path.append(node)
        elif plateau:
            print("\nPlateau reached")
            break
        else:
            print("\nLocal optimum reached")
            break
        
    print("Sequence of visited nodes: ", "->".join(path))
        

HillClimbing()        