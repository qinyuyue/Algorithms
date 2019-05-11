## flood fill
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Algorithm:
        1. from initial pixel, recursion
            if each direction equal to initial value, change to target value
            else: stop
        """
        initial = image[sr][sc]
        if initial == newColor:
            return image
        nr = len(image)
        nc = len(image[0])

        def helper(image, r, c):
            if 0 <= r < nr and 0 <= c < nc:
                if image[r][c] != initial:
                    return
                else:
                    image[r][c] = newColor
                    helper(image, r+1, c)
                    helper(image, r-1, c)
                    helper(image, r, c+1)
                    helper(image, r, c-1)
            return image

        helper(image, sr, sc)
        return image
        
