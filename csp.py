from constraint import Problem, AllDifferentConstraint

class CSP:
    def __init__(self, n):
        self.n = n
        self.sol = [-1] * n
        self.domains =  [list(range(self.n)) for _ in range(self.n)]

        # self.problem = Problem()
        # self._setup()

    # def _setup(self):
    #     cols = range(self.n)
    #     self.problem.addVariables(cols, range(self.n))
    #     self.problem.addConstraint(AllDifferentConstraint())

    #     for col1 in cols:
    #         for col2 in cols:
    #             if col1 < col2:
    #                 self.problem.addConstraint(
    #                     lambda q1, q2, c1=col1, c2=col2: abs(q1 - q2) != abs(c1 - c2),
    #                     (col1, col2)
    #                 )
     
    def isConsidtant(self, sol, row, col):
        for r in range(row):
            c = sol[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True  
    
    
    # def forwardChecking(self, sol, n, row, domains):
    #     placedCol = sol[row]
    #     for r in range(row + 1, n):
    #         newDomains = []
    #         for c in domains[r]:
    #             if self.isConsidtant(sol, r, c):
    #                 newDomains.append(c)
    #         if not newDomains:
    #             return False
    #         domains[r] = newDomains
    #     return True
    def forwardChecking(self, sol, n, row, domains):
        placed_col = sol[row]
        for r in range(row + 1, n):
            newDomains = []
            for c in domains[r]:
                # فقط بررسی با queen فعلی در (row, placed_col)
                if c != placed_col and abs(placed_col - c) != abs(row - r):
                    newDomains.append(c)
            if not newDomains:
                return False
            domains[r] = newDomains
        return True

            
    def backTrack(self, sol, n, row, domains):
        if row == n:
            return sol
            
        for col in domains[row]:
            if self.isConsidtant(sol, row, col):
                sol[row] = col
                newDomains = [list(m) for m in domains]
                if self.forwardChecking(sol, n, row, newDomains):
                    result = self.backTrack(sol, n, row+1, newDomains)
                    if result:
                        return result
                sol[row] = -1
        return None
    
                    
    def solve(self):
        result = self.backTrack(self.sol, self.n, 0, self.domains)
        if result:
            return [x+1 for x in result] 
        
        # return [result[i] + 1 for i in range(self.n)]
        # sol = self.problem.getSolution()
        # if not sol:
        #     return [-1]
        # return [sol[i] + 1 for i in range(self.n)]