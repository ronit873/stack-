class Solution:
    def nextLargerElement(self, arr):
        ans = []
        s = []
        l = len(arr)
        for ele in range(l-1,-1,-1):
            if len(s) == 0:
                ans.append(-1)
            elif s[-1] > arr[ele]:
                ans.append(s[-1])
            else:
                while len(s) > 0 and s[-1] <= arr[ele]:
                    s.pop()
                if len(s) == 0:
                    ans.append(-1)
                else:
                    ans.append(s[-1])
            s.append(arr[ele])
                
        return ans[::-1]