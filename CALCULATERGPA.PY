if not name or not marks_str or not credits_str:
            messagebox.showerror("Error", "Fadlan buuxi meelaha banaan!")
            return
            
        try:
            marks = float(marks_str)
            credits = int(credits_str)
            
            if marks < 0 or marks > 100 or credits <= 0:
                messagebox.showerror("Error", "Dhibcuhu waa 0-100, Credit-kuna waa inuu ka weyn yahay 0!")
                return
        except ValueError:
            messagebox.showerror("Error", "Marks iyo Credits waa inay lambar yihiin!")
            return
            
        grade, points = self.get_grade_points(marks)
        
        self.subjects.append({
            'name': name,
            'marks': marks,
            'grade': grade,
            'points': points,
            'credits': credits
        })
        
        self.tree.config(state=tk.NORMAL)
        self.tree.insert(tk.END, f"{name:<18}{marks:<10}{grade:<10}{credits:<10}\n")
        self.tree.config(state=tk.DISABLED)
        
        self.sub_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)
        self.credit_entry.delete(0, tk.END)
        self.sub_entry.focus()

    def calculate_cgpa(self):
        if not self.subjects:
            messagebox.showwarning("Warning", "Ma jiro coures ad wali galisay")
            return
            
        total_points = 0
        total_credits = 0
        
        for sub in self.subjects:
            total_points += sub['points'] * sub['credits']
            total_credits += sub['credits']
            
        if total_credits == 0:
            cgpa = 0.0
        else:
            cgpa = total_points / total_credits
            
        self.cgpa_label.config(text=f"Final CGPA: {cgpa:.2f}")
        
        if cgpa >= 3.5:
            self.status_label.config(text="Status: Excellent (First Class)", fg="#28a745")
        elif cgpa >= 3.0:
            self.status_label.config(text="Status: Very Good", fg="#007bff")
        elif cgpa >= 2.0:
            self.status_label.config(text="Status: Good (Pass)", fg="#eaff07")
        else:
            self.status_label.config(text="Status: Academic Probation (Fail)", fg="#dc3545")

    def clear_all(self):
        self.subjects = []
        self.tree.config(state=tk.NORMAL)
        self.tree.delete("1.0", tk.END)
        self.tree.insert(tk.END, f"{'Subject':<18}{'Marks':<10}{'Grade':<10}{'Credits':<10}\n" + "-"*48 + "\n")
        self.tree.config(state=tk.DISABLED)
        self.cgpa_label.config(text="Final CGPA: 0.00", fg="#2c3e50")
        self.status_label.config(text="Status: N/A", fg="#7f8c8d")

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeCalculatorApp(root)
    root.mainloop()