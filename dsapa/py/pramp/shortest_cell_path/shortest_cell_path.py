def shortest_cell_path(grid, sr, sc, tr, tc):
    """
    @param grid: int[][]
    @param sr: int
    @param sc: int
    @param tr: int
    @param tc: int
    @return: int
    """
    path = [(sr, sc, 0)]
    max_r = len(grid)
    max_c = len(grid[0])
    visited = {}

    while path:
        r, c, depth = path.pop(0)
        if r == tr and c == tc:
            return depth
        for (nr, nc) in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if (
                0 <= nr < max_r
                and 0 <= nc < max_c
                and grid[nr][nc] == 1
                and (nr, nc) not in visited
            ):
                path.append((nr, nc, depth + 1))
                visited[(r, c)] = True

    return -1


if __name__ == "__main__":
    map_fh = open("map.txt", "r")
    m = []

    for line in map_fh.readlines():
        m.append([int(c) for c in line.rstrip()])

    print(shortest_cell_path(m, 0, 0, 2, 0))
