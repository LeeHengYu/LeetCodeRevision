class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9+7
        a=e=i=o=u=1
        for _ in range(1,n):
            a_n = e
            e_n = (a+i)%MOD
            i_n = (a+e+o+u)%MOD
            o_n = (i+u)%MOD
            u_n = a

            a,e,i,o,u = a_n,e_n,i_n,o_n,u_n

        return (a+e+i+o+u)%MOD