import math

# Alpha-Beta Pruning Function
def alpha_beta(depth, nodeIndex, maximizingPlayer, alpha, beta, height):

    # Base Case: Leaf node reached
    if depth == height:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                alpha,
                beta,
                height
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Beta Cut-off
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                alpha,
                beta,
                height
            )

            best = min(best, value)
            beta = min(beta, best)

            # Alpha Cut-off
            if beta <= alpha:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

height = 3

alpha = -math.inf
beta = math.inf

result = alpha_beta(0, 0, True, alpha, beta, height)

print("Optimal value:", result)   