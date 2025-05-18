from constraint import Problem, AllDifferentConstraint

class CSP:
    def __init__(self, n):
        self.n = n
        self.problem = Problem()
        self._setup()

    def _setup(self):
        cols = range(self.n)
        self.problem.addVariables(cols, range(self.n))

        self.problem.addConstraint(AllDifferentConstraint())

        for col1 in cols:
            for col2 in cols:
                if col1 < col2:
                    self.problem.addConstraint(
                        lambda q1, q2, c1=col1, c2=col2: abs(q1 - q2) != abs(c1 - c2),
                        (col1, col2)
                    )
        
    def solve(self):
        sol = self.problem.getSolution()
        if not sol:
            return [-1]
        return [sol[i] + 1 for i in range(self.n)]