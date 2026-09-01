from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        level = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for deltaI, deltaJ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = i + deltaI, j + deltaJ

                    if ((x, y)) in visited or not (0 <= x < m and 0 <= y < n):
                        continue
                    if grid[x][y] == 2147483647:
                        grid[x][y] = level
                        q.append((x, y))

            level += 1