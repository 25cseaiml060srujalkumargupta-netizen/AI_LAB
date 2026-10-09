from collections import deque

# Check whether a block is clear
def is_clear(state, block):
    for b, position in state:
        if position == block:
            return False
    return True

# Generate possible moves
def generate_moves(state, blocks):
    moves = []

    for block in blocks:
        if not is_clear(state, block):
            continue

        current_position = None
        for b, position in state:
            if b == block:
                current_position = position
                break

        # Move block to Table
        if current_position != "Table":
            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, "Table"))

            moves.append((
                frozenset(new_state),
                f"Move {block} from {current_position} to Table"
            ))

        # Move block onto another block
        for destination in blocks:
            if block == destination:
                continue

            if not is_clear(state, destination):
                continue

            if current_position == destination:
                continue

            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, destination))

            moves.append((
                frozenset(new_state),
                f"Move {block} from {current_position} to {destination}"
            ))

    return moves

# BFS algorithm
def block_world(initial_state, goal_state, blocks):
    queue = deque([(frozenset(initial_state), [])])
    visited = {frozenset(initial_state)}

    while queue:
        current_state, path = queue.popleft()

        if current_state == frozenset(goal_state):
            return path

        for new_state, move in generate_moves(current_state, blocks):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [move]))

    return None

# Main program
print("===== BLOCK WORLD PROBLEM =====")

n = int(input("Enter number of blocks: "))
blocks = []

print("\nEnter block names:")
for i in range(n):
    blocks.append(input(f"Block {i + 1}: "))

# Initial state
print("\n===== INITIAL STATE =====")
print("Enter 'Table' if the block is on the table.")

initial_state = set()
for block in blocks:
    position = input(f"Where is {block} initially? ")
    initial_state.add((block, position))

# Goal state
print("\n===== GOAL STATE =====")
goal_state = set()
for block in blocks:
    position = input(f"Where should {block} be? ")
    goal_state.add((block, position))

# Display states
print("\nInitial State:")
for block, position in sorted(initial_state):
    print(block, "->", position)

print("\nGoal State:")
for block, position in sorted(goal_state):
    print(block, "->", position)

# Find solution
solution = block_world(initial_state, goal_state, blocks)

# Display solution
if solution is not None:
    print("\n===== SOLUTION =====")
    for i, move in enumerate(solution, 1):
        print(f"Step {i}: {move}")

    print("\nTotal moves:", len(solution))
else:
    print("\nNo solution found.")