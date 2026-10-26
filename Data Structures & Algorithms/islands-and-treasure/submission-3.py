from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        INF = 2147483647

        q = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        count = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for deltaI, deltaJ in [(0,1),(0,-1),(1,0),(-1,0)]:
                    newI, newJ = i + deltaI, j + deltaJ

                    if 0 <= newI < m and 0 <= newJ < n and grid[newI][newJ] == INF:
                        grid[newI][newJ] = count
                        q.append((newI, newJ))
            count += 1