
class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        count = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] > 0 and (r, c) not in visited:
                    stack = [(r, c)]
                    visited.add((r, c))
                    total = 0

                    while stack:
                        x, y = stack.pop()
                        total += grid[x][y]

                        directions = [
                            (0, 1),   # right
                            (0, -1),  # left
                            (1, 0),   # down
                            (-1, 0)   # up
                        ]

                        for dx, dy in directions:
                            nx = x + dx
                            ny = y + dy

                            if (0 <= nx < rows and
                                0 <= ny < cols and
                                grid[nx][ny] > 0 and
                                (nx, ny) not in visited):

                                stack.append((nx, ny))
                                visited.add((nx, ny))

                    if total % k == 0:
                        count += 1

        return count
