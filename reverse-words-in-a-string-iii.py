class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split(" ")
        for i in range(len(ls)):
            ls[i] = ls[i][::-1]
        return (" ").join(ls)