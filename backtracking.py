

class Backtracking:
    def __init__(self , n):
        self.n = n
        self.cols = [0] * n
        self.leftDiagonal = [0] * (n * 2)
        self.rightDiagonal = [0] * (n * 2)
        self.sol = []
        
    def back(self, i):
        if i == self.n:
            return True
        
        for j in range(self.n):
            if self.cols[j] or self.leftDiagonal[i - j + self.n - 1] or self.rightDiagonal[i+j]:
                continue
            
            self.cols[j] = 1
            self.leftDiagonal[i - j + self.n - 1] = 1
            self.rightDiagonal[i+j] = 1
            self.sol.append(j + 1)
            
            if self.back(i + 1):
                return True
            
            self.sol.pop()
            self.cols[j] = 0
            self.leftDiagonal[i - j + self.n - 1] = 0
            self.rightDiagonal[i+j] = 0
        
        return False  
    
    def solve(self):
        if self.back(0):
            return self.sol
        else:
            return [-1]
