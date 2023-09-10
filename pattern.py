grid = [
    (0, [1, 3, 4]),
    (1, [0, 3, 4, 5, 2]),
    (2, [1, 4, 5]),
    (3, [0, 1, 4, 7, 6]),
    (4, [0, 1, 2, 3, 5, 6, 7, 8]),
    (5, [2, 1, 4, 7, 8]),
    (6, [3, 4, 7]),
    (7, [6, 3, 4, 5, 8]),
    (8, [5, 4, 7])
]

def recursive(nodes,N):
    if N == 1:
        return sum(len(grid[node][1]) for node in nodes)
    else:
        return sum(recursive(grid[node][1], N - 1) for node in nodes)

pattern_length = int(input('What\'s the length of the pattern lock?: '))

if pattern_length != 1:
    Combination = sum(
        recursive([0, 1, 2, 3, 4, 5, 6, 7, 8], i) for i in range(1, pattern_length+1)
    )
else:
    Combination = recursive([0, 1, 2, 3, 4, 5, 6, 7, 8], 1)

print(Combination)