
test_path = [[0, 0, 0, 0, 0, 0],
             [5, 5, 5, 0, 5, 5],
             [0, 0, 0, 0, 5, 0],
             [0, 5, 5, 0, 0, 9]]


open = []
closed = []

open.append((0, 0))

while open:
    current = open.pop(0)
    i, j = current

    if test_path[i][j] == 9:
        print("Goal found")
        break

    closed.append(current)

    for i, j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if 0 <= i < len(test_path) and 0 <= j < len(test_path[0]):
            if test_path[i][j] != 5 and (i, j) not in closed:
                open.append((i, j))
