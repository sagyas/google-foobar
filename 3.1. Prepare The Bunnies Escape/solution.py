def solution(map):
    height = len(map)
    width = len(map[0])
    min = height * width
    possible_maps = get_all_maps(map)
    possible_maps.append(map)
    for m in possible_maps:
        result = bfs(m)
        if result == height + width - 1:
            return result
        if result < min:
            min = result
    return min


def get_all_maps(map):
    maps = []
    height = len(map)
    width = len(map[0])
    for y in range(height):
        for x in range(width):
            cell = map[y][x]
            if cell == 1:
                copy = [[col for col in row] for row in map]
                copy[y][x] = 0
                maps.append(copy)
    return maps


def bfs(map):
    height = len(map)
    width = len(map[0])
    start = Vertex(0, 0, 1)
    end = Vertex(width-1, height-1)
    queue = []
    dead = []
    queue.append(start)
    while len(queue) != 0:
        cur_v = queue.pop(0)
        if cur_v == end:
            return cur_v.dist
        ngbrs = cur_v.get_ngbrs(map)
        for ngbr in ngbrs:
            if ngbr not in dead and ngbr not in queue:
                queue.append(ngbr)
        dead.append(cur_v)
    return height * width

class Vertex():
    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_ngbrs(self, map):
        ngbrs = []
        x = self.x
        y = self.y
        num_rows = len(map)
        num_cols = len(map[0])
        positions = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        for pos in positions:
            ngbr_x = pos[0]
            ngbr_y = pos[1]
            if ngbr_x >= 0 and ngbr_y >= 0 and ngbr_x < num_cols and ngbr_y < num_rows and map[ngbr_y][ngbr_x] == 0:
                ngbr = Vertex(ngbr_x, ngbr_y, self.dist + 1)
                ngbrs.append(ngbr)
        return ngbrs


# Test
map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
answer = 7
print(solution(map) == answer)

map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
answer = 11
print(solution(map) == answer)
