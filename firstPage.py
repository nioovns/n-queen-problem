import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("N-Queens Solver")
        self.geometry("500x500")

        self.alg_var = tk.StringVar(value="backtrack")
        self.n_var = tk.StringVar()

        # title
        tk.Label(self, text="Choose Algorithm:", font=("Arial", 16)).pack(pady=5)

        # options
        tk.Radiobutton(self, text="Backtracking", variable=self.alg_var, value="backtrack").pack(anchor="w", padx=50)
        tk.Radiobutton(self, text="genetic", variable=self.alg_var, value="genetic").pack(anchor="w", padx=50)
        tk.Radiobutton(self, text="CSP", variable=self.alg_var, value="csp").pack(anchor="w", padx=50)

        # input number
        tk.Label(self, text="Enter N:", font=("Arial", 16)).pack(pady=10)
        tk.Entry(self, textvariable=self.n_var).pack()

        # butten
        tk.Button(self, text="Solve", command=self.solve).pack(pady=15)

    def solve(self):
        algo = self.alg_var.get()
        try:
            n = int(self.n_var.get())
            if n < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for N.")
            return 

        if algo == "backtrack":
            solution = backtracking(n)
            if solution[0] == -1:
                messagebox.showinfo("Result", f"No solution for N={n}")
            else:
                ChessBoard(n, solution)
                
                
        elif algo == "genetic":      
            solution = generic(n)
            if solution[0] == -1:
                messagebox.showinfo("Result", f"No solution for N={n}")
            else:
                ChessBoard(n, solution)
                
                
        else:  
            solution = CSP(n)
            if solution[0] == -1:
                messagebox.showinfo("Result", f"No solution for N={n}")
            else:
                ChessBoard(n, solution)    
                
                     
if __name__ == "__main__":
    app = App()
    app.mainloop()
