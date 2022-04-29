class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dr = [1, -1, 0, 0]
        dc = [0, 0, -1, 1]

        check = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    check[i][j] = True

        def visit(r: int, c: int) -> None:
            check[r][c] = True
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < rows and 0 <= nc < cols and check[nr][nc] == False:
                    visit(nr, nc)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if check[i][j] == False and grid[i][j] == '1':
                    visit(i, j)
                    count += 1

        return count
