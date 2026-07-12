from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # Queue stores ALL currently rotten oranges.
        # This is Multi-source BFS.
        q = deque()

        # time = minutes passed
        # fresh = number of fresh oranges remaining
        time = 0
        fresh = 0

        ROWS, COLS = len(grid), len(grid[0])

        # ----------------------------
        # First pass through the grid
        # ----------------------------
        for r in range(ROWS):
            for c in range(COLS):

                # Count all fresh oranges
                if grid[r][c] == 1:
                    fresh += 1

                # Put every rotten orange into the queue
                # They ALL start spreading at minute 0
                elif grid[r][c] == 2:
                    q.append((r, c))

        # Right, Left, Down, Up
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # Keep spreading while:
        # 1. We still have rotten oranges that can spread
        # 2. Fresh oranges still exist
        while q and fresh > 0:

            # IMPORTANT:
            # len(q) = number of oranges rotten at THIS minute.
            # Process exactly these oranges before increasing time.
            for _ in range(len(q)):

                r, c = q.popleft()

                # Visit all 4 neighbours
                for dr, dc in directions:

                    row = r + dr
                    col = c + dc

                    # Skip if:
                    # - outside the grid
                    # - not a fresh orange
                    if (row < 0 or row >= ROWS or
                        col < 0 or col >= COLS or
                        grid[row][col] != 1):
                        continue

                    # Rot the fresh orange
                    grid[row][col] = 2

                    # It'll spread in the NEXT minute
                    q.append((row, col))

                    # One less fresh orange remains
                    fresh -= 1

            # Entire BFS level finished
            # => One minute has passed
            time += 1

        # If fresh oranges remain,
        # they were unreachable.
        return time if fresh == 0 else -1