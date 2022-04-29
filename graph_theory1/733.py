class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        if image[sr][sc] == newColor:
            return image

        rows = len(image)
        cols = len(image[0])

        dr = [1, -1, 0, 0]
        dc = [0, 0, -1, 1]

        def logic(r: int, c: int):
            target = image[r][c]
            image[r][c] = newColor
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == target:
                    logic(nr, nc)

        logic(sr, sc)

        return image
