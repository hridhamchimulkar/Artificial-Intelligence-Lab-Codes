c1 = int(input("Enter capacity of Jug 1: "))
c2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def waterjug():
    if target % gcd(c1, c2) != 0 or target > max(c1, c2):
        print("\nNo solution exists")
        return
    
    sol_count = 0
    queue = [((0, 0), [(0, 0)])]
    #visited = set() - if only distinct final states are required
    
    while queue:
        (a, b), path = queue.pop(0)
        
        if a == target or b == target:
            sol_count += 1
            print(f"\nSolution {sol_count}: ", path)
            continue
        
        nextStates = [(a, 0), (a, c2), (0, b), (c1, b), (max(0, a - (c2 - b)), min(c2, a + b)), (min(c1, a + b), max(0, b - (c1 - a)))]
        
        for state in nextStates:
            if state not in path:   #if state not in visited - if only distinct final states are required
                queue.append((state, path + [state]))
                #visited.add(state) - if only distinct final states are required
                
                
waterjug()