class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for  i in points:
            i.insert(0, i[0]**2 + i[1]**2)
        points.sort()
        for _ in range(k):
            res.append(points.pop(0)[1:])
        return res
