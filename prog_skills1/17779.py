class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        n = len(points)
        min_idx = -1
        min_val = float("inf")
        for i in range(n):
            if points[i][0] == x or points[i][1] == y:
                dist = abs(points[i][0] - x) + abs(points[i][1] - y)
                if dist < min_val:
                    min_val = dist
                    min_idx = i
        return min_idx
