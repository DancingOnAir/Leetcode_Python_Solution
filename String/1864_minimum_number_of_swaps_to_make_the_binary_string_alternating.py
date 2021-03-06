class Solution:
    # greedy
    def minSwaps(self, s: str) -> int:
        ones = s.count('1')
        zeros = len(s) - ones

        if abs(ones - zeros) > 1:
            return -1

        def helper(x):
            diff = 0
            for c in s:
                if c != x:
                    diff += 1
                x = '1' if x == '0' else '0'
            return diff // 2

        if ones > zeros:
            return helper('1')
        elif ones < zeros:
            return helper('0')
        return min(helper('1'), helper('0'))

    def minSwaps1(self, s: str) -> int:
        n = len(s)
        ones = sum(1 for c in s if c == '1')
        zeros = n - ones

        if abs(ones - zeros) > 1:
            return -1

        def helper(target):
            diff = 0
            for i in range(n):
                if s[i] != target[i]:
                    diff += 1

            return diff // 2

        if ones - zeros == 1:
            alternating = '10' * (n // 2) + '1' + '01' * (n // 2)
            res = helper(alternating)
        elif zeros - ones == 1:
            alternating = '01' * (n // 2) + '0' + '10' * (n // 2)
            res = helper(alternating)
        else:
            res = min(helper('01' * (n // 2)), helper('10' * (n // 2)))
        return res


def test_min_swaps():
    solution = Solution()
    assert solution.minSwaps('111000') == 1, 'wrong result'
    assert solution.minSwaps('010') == 0, 'wrong result'
    assert solution.minSwaps('1110') == -1, 'wrong result'


if __name__ == '__main__':
    test_min_swaps()

