from typing import List


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        dp = [[[''] for _ in range(destination[1] + 1)] for _ in range(destination[0] + 1)]
        for i in range(1, destination[0] + 1):
            dp[i][0] = [x + 'V' for x in dp[i - 1][0]]

        for i in range(1, destination[1] + 1):
            dp[0][i] = [x + 'H' for x in dp[0][i - 1]]

        for i in range(1, destination[0] + 1):
            for j in range(1, destination[1] + 1):
                dp[i][j] = [x + 'V' for x in dp[i - 1][j]]
                dp[i][j] += [x + 'H' for x in dp[i][j - 1]]

        dp[destination[0]][destination[1]].sort()
        return dp[destination[0]][destination[1]][k - 1]


def test_kth_smallest_path():
    solution = Solution()

    destination1 = [2, 3]
    k1 = 1
    res1 = "HHHVV"
    assert solution.kthSmallestPath(destination1, k1) == res1, "wrong result"

    destination2 = [2, 3]
    k2 = 2
    res2 = "HHVHV"
    assert solution.kthSmallestPath(destination2, k2) == res2, "wrong result"

    destination3 = [2, 3]
    k3 = 3
    res3 = "HHVVH"
    assert solution.kthSmallestPath(destination3, k3) == res3, "wrong result"


if __name__ == '__main__':
    test_kth_smallest_path()
