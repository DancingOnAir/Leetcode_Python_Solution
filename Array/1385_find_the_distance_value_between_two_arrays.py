from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()

        def is_valid(num):
            left, right = 0, len(arr2)
            while left < right:
                mid = (left + right) // 2
                if abs(arr2[mid] - num) <= d:
                    return False
                elif arr2[mid] > num:
                    right = mid
                else:
                    left = mid + 1
            return True

        return sum(is_valid(x) for x in arr1)

    def findTheDistanceValue2(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return sum(all(abs(a - b) > d for b in arr2) for a in arr1)

    def findTheDistanceValue1(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = len(arr1)
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if arr2[j] - d <= arr1[i] <= arr2[j] + d:
                    res -= 1
                    break

        return res


def test_find_the_distance_value():
    solution = Solution()

    arr11 = [4, 5, 8]
    arr12 = [10, 9, 1, 8]
    d1 = 2
    print(solution.findTheDistanceValue(arr11, arr12, d1))

    arr21 = [1, 4, 2, 3]
    arr22 = [-4, -3, 6, 10, 20, 30]
    d2 = 3
    print(solution.findTheDistanceValue(arr21, arr22, d2))

    arr31 = [2, 1, 100, 3]
    arr32 = [-5, -2, 10, -3, 7]
    d3 = 6
    print(solution.findTheDistanceValue(arr31, arr32, d3))


if __name__ == '__main__':
    test_find_the_distance_value()

