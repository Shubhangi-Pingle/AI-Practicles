print("Enter the initial state:")
initial_state = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input("Enter tile: ")))
    initial_state.append(row)

# Get goal state from the user
print("Enter the goal state:")
goal_state = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input("Enter tile: ")))
    goal_state.append(row)


def heuri(state, goal_state):
    # Increment h whenever initial[i][j] != goal[i][j]
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                h += 1
    return h

def get_neighbors(state):
    neighbors = []
    zero_i, zero_j = find_zero_position(state)

    for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = zero_i + move[0], zero_j + move[1]

        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[zero_i][zero_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[zero_i][zero_j]
            neighbors.append(new_state)

    return neighbors

def find_zero_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def astar(initial_state, goal_state):
    open_list = [(initial_state, 0, heuri(initial_state, goal_state))]
    closed_list = []

    while open_list:
        current_state, g, h = min(open_list, key=lambda x: x[1] + x[2])
        open_list.remove((current_state, g, h))

        if current_state == goal_state:
            return current_state, g + h  # Return both state and f value

        closed_list.append(current_state)

        neighbors = get_neighbors(current_state)
        for neighbor in neighbors:
            if neighbor in closed_list:
                continue

            neighbor_h = heuri(neighbor, goal_state)
            # f = g + 1 + neighbor_h

            if (neighbor, g + 1, neighbor_h) not in open_list:
                open_list.append((neighbor, g + 1, neighbor_h))

    return None, None

def print_solution(solution_state, f):
    if solution_state is None:
        print("No solution found.")
        return

    print("Solution:")
    print_state(solution_state)
    print("Total cost (f):", f)



def print_state(state):
    for i in range(3):
        for j in range(3):
            print(state[i][j],end=" ")
        print()
# Solve using A* algorithm
solution_state, f_value = astar(initial_state, goal_state)

# Print the solution and f value
print_solution(solution_state, f_value)
