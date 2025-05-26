import tkinter as tk
from tkinter import messagebox
from ChessBoard import ChessBoard
from csp import CSP
from GeneticAlgorithm import genetic_algorithm
from backtracking import Backtracking

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("N-Queens Solver")
        self.geometry("500x450")
        self.configure(bg="white")

        self.alg_var = tk.StringVar(value="genetic")
        self.n_var = tk.StringVar()

        tk.Label(self, text="N-Queen", font=("Arial", 24, "bold"),fg="purple", bg="white").pack(pady=5)
        
        tk.Frame(self, height=2, bg="black").pack(fill="x", padx=10, pady=5)
        
        tk.Label(self, text="Choose your algorithm:", font=("Arial", 18), bg="white").pack(pady=10)

        tk.Radiobutton(self, text="Backtracking", variable=self.alg_var, value="backtrack", bg="white", font=("Aria", 14)).pack(anchor="center")
        tk.Radiobutton(self, text="Genetic", variable=self.alg_var, value="genetic", bg="white", font=("Aria", 14)).pack(anchor="center")
        tk.Radiobutton(self, text="CSP", variable=self.alg_var, value="csp", bg="white", font=("Aria", 14)).pack(anchor="center")

        tk.Frame(self, height=2, bg="black").pack(fill="x", padx=10, pady=5)

        tk.Label(self, text="Enter your number:", font=("Arial", 18), bg="white").pack(anchor="center")

   
        input_frame = tk.Frame(self, bg="white", highlightbackground="black", highlightthickness=2, bd=0)
        input_frame.pack(pady=10)

       
        tk.Entry(input_frame, textvariable=self.n_var, font=("Arial", 12), width=10).pack(side="left", padx=5)

        canvas = tk.Canvas(self, width=85, height=150, highlightthickness=0, bg="white")
        canvas.pack()

        circle = canvas.create_oval(10, 10, 80, 80, fill="#df80ff", outline="#000000")
        icon = canvas.create_text(49, 45, text="▶", font=("Arial", 45), fill="black")

        def on_circle_click(event=None):
            self.solve()

        canvas.tag_bind(circle, "<Button-1>", on_circle_click)
        canvas.tag_bind(icon, "<Button-1>", on_circle_click)

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
            solver = Backtracking(n)
            solution = solver.solve()
            if solution[0] == -1:
                messagebox.showinfo("Result", f"No solution for N={n}")
            else:
                ChessBoard(n, solution)

        elif algo == "genetic":
            solution = genetic_algorithm(n)
            if solution:
                ChessBoard(n, solution.genes)
            elif solution is None:
                messagebox.showinfo("Result", f"No solution for N={n}")
                
        else:  
            solver = CSP(n)
            solution = solver.solve()
            if solution is None:
                messagebox.showinfo("Result", f"No solution for N={n}")
            else:
                ChessBoard(n, solution) 


if __name__ == "__main__":
    app = App()
    app.mainloop()