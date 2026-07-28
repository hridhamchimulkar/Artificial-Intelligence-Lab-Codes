def valid(state):
    m, c, b = state
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if (m > 0 and m < c) or ((3 - m) > 0 and (3 - m) < (3 - c)): 
        return False
    return True


def MissionariesAndCannibals():
    sol_count = 0
    start = (3, 3, 'L')
    stack = [(start, [start])]
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    while stack:
        (m, c, b), path = stack.pop()
        
        if (m, c, b) == (0, 0, 'R'):
            sol_count += 1
            print(f"\nSolution {sol_count}:")
            for state in path:
                print(state)
            continue
        
        for moveM, moveC in moves:
            if b == 'L':
                newState = (m - moveM, c - moveC, 'R')
            else:
                newState = (m + moveM, c + moveC, 'L')
                
            if valid(newState) and newState not in path:
                stack.append((newState, path + [newState]))
                

MissionariesAndCannibals()