# import pdb
# from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def normalize(grid):
    """
    Given a grid of unnormalized probabilities, computes the
    correspond normalized version of that grid.
    """
    total = 0.0
    for row in grid:
        for cell in row:
            total += cell
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            grid[i][j] = float(cell) / total
    return grid


def sense2D(measurement, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    for i, row in enumerate(grid):
        new_beliefs.append(
            [beliefs[i][j] * ((measurement == cell) * p_hit + (measurement != cell) * p_miss)
             for j, cell in enumerate(row)]
        )
    return normalize(new_beliefs)


def move2D(dy, dx, beliefs, p_move):
    new_beliefs = []
    height = len(beliefs)
    width = len(beliefs[0])
    for i in range(height):
        new_beliefs.append(
            [beliefs[(i - dy) % height][(j - dx) % width] * p_move +
             beliefs[i][j] * (1 - p_move)
             for j in range(width)]
        )
    return new_beliefs


def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy) % width
            new_j = (j + dx) % height
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
            # return blur(new_G, blurring)


def localize(colors, measurements, motions, sensor_right, p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    for i, measurement in enumerate(measurements):
        p = move2D(motions[i][0], motions[i][1], beliefs=p, p_move=p_move)
        p = sense2D(measurement=measurement, grid=colors, beliefs=p, p_hit=sensor_right, p_miss=1 - sensor_right)
    return p


def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x), r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')


colors = [['R', 'G', 'G', 'R', 'R'],
          ['R', 'R', 'G', 'R', 'R'],
          ['R', 'R', 'G', 'G', 'R'],
          ['R', 'R', 'R', 'R', 'R']]
measurements = ['G', 'G', 'G', 'G', 'G']
motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]
p = localize(colors, measurements, motions, sensor_right=0.7, p_move=0.8)
show(p)

# test 7
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 1.0
p_move = 0.5
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 0.33333333, 0.66666666],
     [0.0, 0.0, 0.0]])
show(p)
