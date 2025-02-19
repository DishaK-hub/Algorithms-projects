import queue

def ShortestPath(goal, initial):
    def move(state, direction):
        # Helper function to move the empty cell in the given direction if it's a valid move
        new_state = list(state)
        empty_idx = new_state.index(0)
        if direction == 'U' and empty_idx >= 3:
            new_state[empty_idx], new_state[empty_idx - 3] = new_state[empty_idx - 3], new_state[empty_idx]
        elif direction == 'D' and empty_idx < 6:
            new_state[empty_idx], new_state[empty_idx + 3] = new_state[empty_idx + 3], new_state[empty_idx]
        elif direction == 'L' and empty_idx % 3 != 0:
            new_state[empty_idx], new_state[empty_idx - 1] = new_state[empty_idx - 1], new_state[empty_idx]
        elif direction == 'R' and empty_idx % 3 != 2:
            new_state[empty_idx], new_state[empty_idx + 1] = new_state[empty_idx + 1], new_state[empty_idx]

        return tuple(new_state)

    def bfs(initial_state, goal_state):
        visited = set()
        q = [(initial_state, 0)]  # (state, steps)
        while q:
            current_state, steps = q.pop(0)  # Pop from the front of the list
            if current_state == goal_state:
                return steps
            if current_state in visited:
                continue
            visited.add(current_state)
            for direction in ['U', 'D', 'L', 'R']:
                new_state = move(current_state, direction)
                if new_state is not None:  # Check if the move is valid
                    q.append((new_state, steps + 1))
        return -1  # No solution found

    goal_state = tuple(goal)
    shortest_paths = []
    for initial_state in initial:
        initial_state = tuple(initial_state)
        path_length = bfs(goal_state, initial_state)
        shortest_paths.append(path_length)

    return shortest_paths

# Example usage:
if __name__ == "__main__":

    # initial_states = [[1, 2, 3, 8, 0, 4, 7, 6, 5]]
    # goal_state = [1, 3, 4, 8, 6, 2, 7, 0, 5]
    #
    # initial_states = [[1,2,3,8,0,4,7,6,5]]
    # goal_state = [2,8,1,0,4,3,7,6,5]

    # initial_states = [
    #     [1, 2, 3, 8, 0, 4, 7, 6, 5]
    # ]
    #
    # goal_state = [2, 8, 1, 4, 6, 3, 0, 7, 5]

    # initial_states = [
    #     [1,3,4,8,0,5,7,2,6],
    #     [2,3,1,7,0,8,6,5,4],
    #     [2,3,1,8,0,4,7,6,5],
    #     [2,8,3,1,0,4,7,6,5],
    #     [8,7,6,1,0,5,2,3,4]
    #     ]
    #
    # goal_state = [1,2,3,8,0,4,7,6,5]
    #
    # initial_states = [
    #     [8,6,7,2,5,4,3,0,1],
    #     [6,4,7,8,5,0,3,2,1],
    #     [4,1,2,0,8,7,6,3,5],
    #     [1,6,2,5,7,3,0,4,8]
    # ]
    #
    # goal_state = [1,2,3,4,5,6,7,8,0]

    initial_states = [
        [8, 0, 6, 5, 4, 7, 2, 3, 1],
        [6, 4, 1, 3, 0, 2, 7, 5, 8],
        [1, 5, 8, 3, 2, 7, 0, 6, 4],
        [3, 2, 8, 4, 5, 1, 6, 7, 0],
        [0, 3, 5, 4, 2, 8, 6, 1, 7],
        [7, 2, 5, 3, 1, 0, 6, 4, 8]
    ]

    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    print(ShortestPath(goal_state, initial_states))