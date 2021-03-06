from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = 0, 0

        for num in nums:
            if num >= first:
                first, second = num, first
            elif num > second:
                second = num
        return (first - 1) * (second - 1)

    def maxProduct1(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)


def test_max_product():
    solution = Solution()

    nums1 = [3, 4, 5, 2]
    print(solution.maxProduct(nums1))

    nums2 = [1, 5, 4, 5]
    print(solution.maxProduct(nums2))

    nums3 = [3, 7]
    print(solution.maxProduct(nums3))


if __name__ == '__main__':
    test_max_product()
