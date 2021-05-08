from itertools import groupby


class Solution:
    def maxPower(self, s: str) -> int:
        return max([len(list(g)) for k, g in groupby(s)])


def test_max_power():
    solution = Solution()
    assert solution.maxPower('leetcode') == 2, 'wrong result'
    assert solution.maxPower('abbcccddddeeeeedcba') == 5, 'wrong result'
    assert solution.maxPower('triplepillooooow') == 5, 'wrong result'
    assert solution.maxPower('hooraaaaaaaaaaay') == 11, 'wrong result'
    assert solution.maxPower('tourist') == 1, 'wrong result'


if __name__ == '__main__':
    test_max_power()
