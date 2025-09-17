class Solution:
    def isBalanced(self, s):
        brackets = ['[','{','(']
        res = []
        for i in s:
            if i in brackets:
                if i == "[":
                    res.append("]")
                elif i == "{":
                    res.append("}")
                elif i == "(":
                    res.append(")")
            else:
                if not res:
                    return False
                index = len(res)-1
                if i == res[index]:
                    res.pop(index)
                else:
                    return False
        if res == []:
            return True
        else:
            return False