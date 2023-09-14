def check_card(grid1, grid2):
    for counti, i in enumerate(grid1):
        for countj, j in enumerate(i):
            if j != grid2[counti][countj]:
                return 0
    return 1

def map_grid(grid, size, x_corner, y_corner):
    fgrid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(grid[x_corner+i][y_corner+j])
        fgrid.append(row)
    return fgrid

def rotate_grid(grid):
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0])-1,-1,-1)]

def move_grid(grid, grades):
    if grades == '270':
        return rotate_grid(grid)
    elif grades == '180':
        return rotate_grid(rotate_grid(grid))
    elif grades == '90':
        return rotate_grid(rotate_grid(rotate_grid(grid)))

with open('../input/input9.txt') as f:
    l = f.readline().strip().split(' ')
    c, p = int(l[0]), int(l[1])
    card_grid = []
    pad_grid = []
    for i in range(c):
        row = list(f.readline().strip())
        card_grid.append(row)
    for i in range(p):
        row = list(f.readline().strip())
        pad_grid.append(row)

max_attempts = p-c+1
pos_array = ['90','180','270']
found = 0

for i in range(max_attempts):
    for j in range(max_attempts):
        mapped_grid = map_grid(pad_grid, c, i, j)
        if check_card(card_grid, mapped_grid):
            print(f'{i} {j} 0')
            found = 1
        else:
            for _ in pos_array:
                if check_card(move_grid(card_grid, _), mapped_grid):
                    print(f'{i} {j} {_}')
                    found = 1
        if found == 1:
            break
    if found == 1:
        break
                    

if found == 0:
    print('err')