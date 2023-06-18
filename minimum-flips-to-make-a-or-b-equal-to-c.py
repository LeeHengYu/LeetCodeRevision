class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = format(a, 'b')
        b = format(b, 'b')
        c = format(c, 'b')

        n = max(len(a), len(b), len(c))
        while len(a) < n:
            a = '0' + a
        while len(b) < n:
            b = '0' + b
        while len(c) < n:
            c = '0' + c

        res = 0
        for i in range(n):
            if c[i] == '1' and a[i] == '0' and b[i] == '0':
                res += 1
            if c[i] == '0':
                if a[i] == '1':
                    res += 1
                if b[i] == '1':
                    res += 1
        return res
