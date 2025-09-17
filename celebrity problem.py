class Solution:
    def celebrity(self, mat):
        
        potentials = []
        for idx, i in enumerate(mat):
            if sum(i) ==1:
                potentials.append(idx)
        n = len(mat)
                
        for p in potentials:
            i =0
            while i< n:
                if mat[i][p] ==0:
                    break
                elif i ==n-1:
                    return p
                i+=1
        return -1