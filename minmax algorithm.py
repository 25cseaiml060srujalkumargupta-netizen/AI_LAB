# Minimax Algorithm
def minimax(depth, nodeIndex, isMax, scores, height):
    # Base Case: Leaf node reached
    if depth == height:
        return scores[nodeIndex]
    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, scores, height)
        )
# Main Program
scores = list(map(int, input("Enter 8 leaf node values: ").split()))
height = 3
result = minimax(0, 0, True, scores, height)
print("\nThe optimal value is:", result)
