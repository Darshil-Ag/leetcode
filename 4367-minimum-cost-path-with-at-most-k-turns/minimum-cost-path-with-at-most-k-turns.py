import heapq

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0, 0, -1))  # CHANGED: initial direction
        minn = float('inf')
        m = len(grid)
        n = len(grid[0])
        vis = {}  # ADDED: best cost for each state

        while pq:
            dist, turns, i, j, curr = heapq.heappop(pq)

            if turns > k:
                continue

            state = (i, j, turns, curr)  # ADDED
            if state in vis and vis[state] <= dist:  # ADDED
                continue
            vis[state] = dist  # ADDED

            if i == m-1 and j == n-1:
                return dist  # CHANGED: min-heap guarantees minimum cost

            if curr == -1:  # ADDED: first move can be in any direction
                if i + 1 < m:
                    heapq.heappush(pq, (dist + grid[i+1][j], turns, i+1, j, 0))
                if j + 1 < n:
                    heapq.heappush(pq, (dist + grid[i][j+1], turns, i, j+1, 1))
                if i - 1 >= 0:
                    heapq.heappush(pq, (dist + grid[i-1][j], turns, i-1, j, 3))
                if j - 1 >= 0:
                    heapq.heappush(pq, (dist + grid[i][j-1], turns, i, j-1, 2))

            elif curr == 0:
                if i + 1 < m:
                    heapq.heappush(pq, (dist + grid[i+1][j], turns, i+1, j, 0))
                if j + 1 < n:
                    heapq.heappush(pq, (dist + grid[i][j+1], turns+1, i, j+1, 1))
                if i - 1 >= 0:
                    heapq.heappush(pq, (dist + grid[i-1][j], turns+1, i-1, j, 3))
                if j - 1 >= 0:
                    heapq.heappush(pq, (dist + grid[i][j-1], turns+1, i, j-1, 2))

            elif curr == 1:
                if i + 1 < m:
                    heapq.heappush(pq, (dist + grid[i+1][j], turns+1, i+1, j, 0))
                if j + 1 < n:
                    heapq.heappush(pq, (dist + grid[i][j+1], turns, i, j+1, 1))
                if i - 1 >= 0:
                    heapq.heappush(pq, (dist + grid[i-1][j], turns+1, i-1, j, 3))
                if j - 1 >= 0:
                    heapq.heappush(pq, (dist + grid[i][j-1], turns+1, i, j-1, 2))

            elif curr == 2:
                if i + 1 < m:
                    heapq.heappush(pq, (dist + grid[i+1][j], turns+1, i+1, j, 0))
                if j + 1 < n:
                    heapq.heappush(pq, (dist + grid[i][j+1], turns+1, i, j+1, 1))
                if i - 1 >= 0:
                    heapq.heappush(pq, (dist + grid[i-1][j], turns+1, i-1, j, 3))
                if j - 1 >= 0:
                    heapq.heappush(pq, (dist + grid[i][j-1], turns, i, j-1, 2))

            elif curr == 3:
                if i + 1 < m:
                    heapq.heappush(pq, (dist + grid[i+1][j], turns+1, i+1, j, 0))
                if j + 1 < n:
                    heapq.heappush(pq, (dist + grid[i][j+1], turns+1, i, j+1, 1))
                if i - 1 >= 0:
                    heapq.heappush(pq, (dist + grid[i-1][j], turns, i-1, j, 3))
                if j - 1 >= 0:
                    heapq.heappush(pq, (dist + grid[i][j-1], turns+1, i, j-1, 2))

        return -1