

class CSP:
    def __init__(self, n):
        self.n = n
        self.variables = list(range(n))  #row
        self.domains = {var: list(range(n)) for var in self.variables} # for every row, all cols that you can adjust a queen 
        self.assignment = {}
     
     
    def isConsitent(self, var, val):
        for other_var in self.assignment:
            other_val = self.assignment[other_var]
            if val == other_val or abs(var - other_var) == abs(val - other_val):
                return False
        return True
    
    
    def forwardChecking(self, var, val, domains):
        newDomain = {v: list(domains[v]) for v in domains}
        for other_var in self.variables:
            if other_var not in self.assignment and val in newDomain[other_var]:
                if var == other_var:
                    continue
                try:
                    newDomain[other_var].remove(val)
                except ValueError:
                    pass
                diag1 = val + (other_var - var)
                diag2 = val - (other_var - var)
                for d in [diag1, diag2]:
                    if d in newDomain[other_var]:
                        newDomain[other_var].remove(d)
                if not newDomain[other_var]: 
                    return None
        return newDomain
    
    
    def selectUnassignedVar(self, domains):
        unassigned = [v for v in self.variables if v not in self.assignment]
        return min(unassigned, key=lambda var: len(domains[var]))
            
            
    def backtrack(self, domains):
        if len(self.assignment) == self.n:
            return self.assignment

        var = self.selectUnassignedVar(domains)
        for val in domains[var]:
            if self.isConsitent(var, val):
                self.assignment[var] = val
                newDomain = self.forwardChecking(var, val, domains)
                if newDomain is not None:
                    result = self.backtrack(newDomain)
                    if result:
                        return result
                del self.assignment[var]
        return None
                    
    def solve(self):
        result = self.backtrack(self.domains)
        if result:
            return [result[i] + 1 for i in range(self.n)]
        return [-1]   