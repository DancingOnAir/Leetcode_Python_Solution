from collections import deque


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res, cur = 0, 0
        counter = set()
        vowels = set('aeiou')

        for i, c in enumerate(word):
            if i and word[i - 1] > c:
                counter = set()
                cur = 0

            counter.add(c)
            cur += 1
            if len(counter) == 5:
                res = max(res, cur)
        return res


def test_longest_beautiful_substring():
    solution = Solution()
    assert solution.longestBeautifulSubstring('aeiaaioaaaaeiiiiouuuooaauuaeiu') == 13, 'wrong result'
    assert solution.longestBeautifulSubstring('aeeeiiiioooauuuaeiou') == 5, 'wrong result'
    assert solution.longestBeautifulSubstring('a') == 0, 'wrong result'


if __name__ == '__main__':
    test_longest_beautiful_substring()
