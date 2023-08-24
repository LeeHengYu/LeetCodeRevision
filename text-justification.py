class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        res = []
        line, length = [], 0
        while i<len(words):
            if length+len(line)+len(words[i])>maxWidth:
                extraspaces = (maxWidth-length) // max(len(line)-1,1)
                remainder  = (maxWidth-length) % max(len(line)-1,1)
                for j in range(max(1, len(line)-1)): 
                    line[j] += " "  * extraspaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                line = []
                length = 0

            line.append(words[i])
            length += len(words[i])
            i+=1
        # last line
        extraspaces = (maxWidth-length) // max(len(line)-1,1)
        if len(line)==1:
            res.append(line[0]+" "*(maxWidth-len(line[0])))
        else:
            for i in range(len(line)-1):
                line[i]+=" "
            temp = "".join(line)
            remain = maxWidth-len(temp)
            temp += " "*remain
            res.append(temp)

        return res    