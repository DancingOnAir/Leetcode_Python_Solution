from collections import defaultdict
from copy import deepcopy
from collections import Counter


class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        res = 0
        for i in range(n - 2):
            for j in range(2, n - i + 1):
                c = Counter(s[i: i + j])
                res += c.most_common()[0][1] - c.most_common()[-1][1]

        return res


def test_beauty_sum():
    solution = Solution()
    assert solution.beautySum('aabcb') == 5, 'wrong result'
    assert solution.beautySum('aabcbaa') == 17, 'wrong result'


if __name__ == '__main__':
    test_beauty_sum()
