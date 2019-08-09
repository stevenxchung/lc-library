'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
'''

points = [[1, 3], [-2, 2]]
K = 1
# points = [[3, 3], [5, -1], [-2, 4]]
# K = 2
# points = [[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [1, 1]]
# K = 1
# points = [[0, 1], [1, 0]]
# K = 2


# class Solution:
#     def kClosest(self, points, K):
#         output = []
#         distArr = []
#         limit = 0

#         # Calculate distance for each pair
#         for i, pair in enumerate(points):
#             # Equation for Euclidean distance
#             dist = (pair[0]**2 + pair[1]**2)**(1/2)
#             distArr.append([dist, i])

#         # Sort distances from small to large
#         distArr = sorted(distArr, key=lambda x: x[0])

#         # Append each pair to output array based on distance
#         for distPair in distArr:
#             if limit != K:
#                 output.append(points[distPair[1]])
#             else:
#                 break
#             limit += 1

#         return output


# sol = Solution()
# print(sol.kClosest(points, K))
