from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        buckets = [0] * 10001
        max_num = 0
        for num in nums:
            max_num = max(max_num, num)
            buckets[num] += num

        if max_num < 1:
            return 0

        dp = [0] * (max_num + 1)
        dp[1] = buckets[1]
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + buckets[i])
        return dp[max_num]

    def deleteAndEarn3(self, nums: List[int]) -> int:
        points, prev, curr = Counter(nums), 0, 0
        for val in range(10001):
            prev, curr = curr, max(prev + points[val] * val, curr)
        return curr

    def deleteAndEarn2(self, nums: List[int]) -> int:
        points = Counter(nums)
        j, prev, curr = -1, 0, 0
        for i in sorted(points.keys()):
            if i - j > 1:
                prev, curr = curr, curr + points[i] * i
            else:
                prev, curr = curr, max(curr, prev + points[i] * i)
            j = i
        return curr

    def deleteAndEarn1(self, nums: List[int]) -> int:
        values = [0] * 10001
        for num in nums:
            values[num] += num

        take, skip = 0, 0
        for i in range(10001):
            take_i = skip + values[i]
            skip_i = max(take, skip)

            take = take_i
            skip = skip_i

        return max(take, skip)


def test_delete_and_earn():
    solution = Solution()

    nums1 = [3, 4, 2]
    assert solution.deleteAndEarn(nums1) == 6, 'wrong result'

    nums2 = [2, 2, 3, 3, 3, 4]
    assert solution.deleteAndEarn(nums2) == 9, 'wrong result'

    nums3 = [8, 7, 3, 8, 1, 4, 10, 10, 10, 2]
    assert solution.deleteAndEarn(nums3) == 52, 'wrong result'


if __name__ == '__main__':
    test_delete_and_earn()
