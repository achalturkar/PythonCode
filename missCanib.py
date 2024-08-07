def is_valid_state(state):
    m, c, b = state
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:  
        return False
    if m < 3 and (3 - m) < (3 - c):  
        return False
    return True

def get_successors(state):
    successors = []
    m, c, b = state
    actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  
    
    for a in actions:
        new_m = m - a[0] * b + a[0] * (1 - b)
        new_c = c - a[1] * b + a[1] * (1 - b)
        new_b = 1 - b
        new_state = (new_m, new_c, new_b)
        if is_valid_state(new_state):
            successors.append(new_state)
    
    return successors

def missionaries_and_cannibals_brute_force():
    initial_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    frontier = [(initial_state, [])]
    explored = set()

    while frontier:
        current_state, path = frontier.pop(0)
        if current_state == goal_state:
            return path + [current_state]

        if current_state in explored:
            continue

        explored.add(current_state)
        for successor in get_successors(current_state):
            if successor not in explored:
                frontier.append((successor, path + [current_state]))

    return None

solution = missionaries_and_cannibals_brute_force()

if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")
