class Solution:
    def modifyString(self, s: str) -> str:
        res, pre = '', '?'
        for i, c in enumerate(s):
            nxt = s[i + 1] if i + 1 < len(s) else '?'
            pre = c if c != '?' else {'a', 'b', 'c'}.difference({pre, nxt}).pop()
            res += pre
        return res

    def modifyString3(self, s: str) -> str:
        n = len(s)
        if 1 == n:
            return 'a'

        s = list(s)
        for i, val in enumerate(s):
            if val == '?':
                for c in 'abc':
                    if (i == 0 or s[i - 1] != c) and (i + 1 == n or s[i + 1] != c):
                        s[i] = c
                        break
        return ''.join(s)

    def modifyString2(self, s: str) -> str:
        n = len(s)
        res = ''
        for i, val in enumerate(s):
            if val == '?':
                for j in range(97, 123):
                    # for cpp
                    # if i - 1 >= 0 and s[i - 1] == chr(j):
                    # for python
                    if i - 1 >= 0 and res[-1] == chr(j):
                        continue
                    if i + 1 < n and s[i + 1] == chr(j):
                        continue

                    res += chr(j)
                    break
            else:
                res += val
        return res

    def modifyString1(self, s: str) -> str:
        res = ''
        pre, cur = -1, 0
        while cur < len(s):
            if s[cur] != '?':
                pre = cur
                res += s[cur]
                cur += 1
            else:
                while cur < len(s) and s[cur] == '?':
                    cur += 1

                base = 97
                if pre != -1:
                    base += ((ord(s[pre]) + 1) - base) % 26

                replace_substring = ''.join([chr(97 + (base + i - 97) % 26) for i in range(cur - pre - 1)])
                if cur < len(s) and s[cur] == replace_substring[-1]:
                    replace_substring = replace_substring[:-1] + chr(ord(s[cur]) + 1 if ord(s[cur]) + 1 != 123 else 97)
                res += replace_substring
        return res


def test_modify_string():
    solution = Solution()
    assert solution.modifyString('?zs') == 'azs', 'wrong result'
    assert solution.modifyString('ubv?w') == 'ubvxw', 'wrong result'
    assert solution.modifyString('j?qg??b') == 'jkqghib', 'wrong result'
    assert solution.modifyString('??yw?ipkj?') == 'abywxipkjk', 'wrong result'
    assert solution.modifyString("b?a") == 'bca', 'wrong result'
    assert solution.modifyString("y?z") == 'yaz', 'wrong result'
    assert solution.modifyString("?y??ty") == "ayzaty", 'wrong result'


if __name__ == '__main__':
    test_modify_string()
