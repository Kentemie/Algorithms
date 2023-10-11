# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some
# of the dominoes either to the left or to the right.

# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes
# falling to the right push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or
# already fallen domino.

# You are given a string dominoes representing the initial state where:

    # dominoes[i] = 'L', if the ith domino has been pushed to the left,
    # dominoes[i] = 'R', if the ith domino has been pushed to the right, and
    # dominoes[i] = '.', if the ith domino has not been pushed.

# Return a string representing the final state.

from collections import deque

def pushDominoes(dominoes):
    queue = deque()
    dominoes = list(dominoes)

    for i, domino in enumerate(dominoes):
        if domino != '.':
            queue.append((i, domino))
    
    while queue:
        i, domino = queue.popleft()
        if domino == 'L' and i > 0 and dominoes[i - 1] == '.':
            queue.append((i - 1, 'L'))
            dominoes[i - 1] = 'L'
        elif domino == 'R' and i < len(dominoes) - 1 and dominoes[i + 1] == '.':
            if i < len(dominoes) - 2 and dominoes[i + 2] == 'L':
                queue.popleft()
            else:
                queue.append((i + 1, 'R'))
                dominoes[i + 1] = 'R'
    
    return "".join(dominoes)

dominoes = ".L.R...LR..L.."

print(pushDominoes(dominoes))