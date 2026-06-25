import tkinter as tk
from tkinter import messagebox

class GradeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade & CGPA Calculator")
        self.root.geometry("450x550")
        self.root.config(bg="#f4f6f9")
        
        self.subjects = []
        
        # Title Label
        title = tk.Label(root, text="Student Grade Calculator", font=("Arial", 16, "bold"), bg="#f4f6f9", fg="#333")
        title.pack(pady=15)
        
        # Input Frame
        input_frame = tk.Frame(root, bg="#f4f6f9")
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Subject Name:", font=("Arial", 10), bg="#f4f6f9").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.sub_entry = tk.Entry(input_frame, font=("Arial", 10), width=20)
        self.sub_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Marks (0-100):", font=("Arial", 10), bg="#f4f6f9").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.marks_entry = tk.Entry(input_frame, font=("Arial", 10), width=20)
        self.marks_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Credit Hours:", font=("Arial", 10), bg="#f4f6f9").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.credit_entry = tk.Entry(input_frame, font=("Arial", 10), width=20)
        self.credit_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Buttons
        btn_frame = tk.Frame(root, bg="#f4f6f9")
        btn_frame.pack(pady=10)
        
        add_btn = tk.Button(btn_frame, text="Add Subject", command=self.add_subject, bg="#28a745", fg="white", font=("Arial", 10, "bold"), width=12)
        add_btn.grid(row=0, column=0, padx=5)
        
        calc_btn = tk.Button(btn_frame, text="Calculate CGPA", command=self.calculate_cgpa, bg="#007bff", fg="white", font=("Arial", 10, "bold"), width=12)
        calc_btn.grid(row=0, column=1, padx=5)
        
        clear_btn = tk.Button(btn_frame, text="Clear All", command=self.clear_all, bg="#dc3545", fg="white", font=("Arial", 10, "bold"), width=12)
        clear_btn.grid(row=0, column=2, padx=5)
        
        # Display Listbox
        self.list_frame = tk.Frame(root)
        self.list_frame.pack(pady=10)
        
        self.tree = tk.Text(self.list_frame, height=10, width=50, font=("Courier", 9))
        self.tree.pack()
        self.tree.insert(tk.END, f"{'Subject':<18}{'Marks':<10}{'Grade':<10}{'Credits':<10}\n" + "-"*48 + "\n")
        self.tree.config(state=tk.DISABLED)
        
        # Result Labels
        self.result_frame = tk.Frame(root, bg="#f4f6f9")
        self.result_frame.pack(pady=15)
        
        self.cgpa_label = tk.Label(self.result_frame, text="Final CGPA: 0.00", font=("Arial", 13, "bold"), bg="#f4f6f9", fg="#2c3e50")
        self.cgpa_label.pack()
        
        self.status_label = tk.Label(self.result_frame, text="Status: N/A", font=("Arial", 11, "bold"), bg="#f4f6f9", fg="#7f8c8d")
        self.status_label.pack(pady=2)

    def get_grade_points(self, marks):
        if marks >= 90: return "A", 4.0
        elif marks >= 80: return "B", 3.0
        elif marks >= 70: return "C", 2.0
        elif marks >= 60: return "D", 1.0
        else: return "F", 0.0

    def add_subject(self):
        name = self.sub_entry.get().strip()
        marks_str = self.marks_entry.get().strip()
        credits_str = self.credit_entry.get().strip()