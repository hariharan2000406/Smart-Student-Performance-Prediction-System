import tkinter as tk

root = tk.Tk()
root.title("Smart Student Performance Prediction System")
root.geometry("700x500")
root.resizable(False, False)
root.configure(bg="#f0f2f5")

# ── header ────────────────────────────────────────────────────────────────────
tk.Label(root,
         text="SMART STUDENT PERFORMANCE\nPREDICTION SYSTEM",
         font=("Arial", 15, "bold"), bg="#f0f2f5", fg="#2c3e50",
         justify="center").pack(pady=(18, 10))

# ── two-column frame ──────────────────────────────────────────────────────────
mid = tk.Frame(root, bg="#f0f2f5")
mid.pack(padx=20, fill="x")

# ── student information frame ─────────────────────────────────────────────────
stu = tk.LabelFrame(mid, text="Student Information",
                    font=("Arial", 10, "bold"), bg="#f0f2f5", fg="#2c3e50",
                    padx=10, pady=10)
stu.grid(row=0, column=0, padx=(0, 10), sticky="nsew")

tk.Label(stu, text="Student ID",   bg="#f0f2f5").grid(row=0, column=0, sticky="w", pady=6)
tk.Label(stu, text="Student Name", bg="#f0f2f5").grid(row=1, column=0, sticky="w", pady=6)

entry_id   = tk.Entry(stu, width=24)
entry_name = tk.Entry(stu, width=24)
entry_id  .grid(row=0, column=1, padx=8)
entry_name.grid(row=1, column=1, padx=8)

# ── academic information frame ────────────────────────────────────────────────
acad = tk.LabelFrame(mid, text="Academic Information",
                     font=("Arial", 10, "bold"), bg="#f0f2f5", fg="#2c3e50",
                     padx=10, pady=10)
acad.grid(row=0, column=1, sticky="nsew")

acad_labels = [
    "Attendance (%)",
    "Study Hours (per day)",
    "Internal Marks (%)",
    "Assignment (%)",
    "Previous Score (%)"
]

entries = {}
for i, lbl in enumerate(acad_labels):
    tk.Label(acad, text=lbl, bg="#f0f2f5").grid(row=i, column=0, sticky="w", pady=4)
    e = tk.Entry(acad, width=18)
    e.grid(row=i, column=1, padx=8)
    entries[lbl] = e

mid.columnconfigure(0, weight=1)
mid.columnconfigure(1, weight=1)

# ── action buttons ────────────────────────────────────────────────────────────
btn_frame = tk.Frame(root, bg="#f0f2f5")
btn_frame.pack(pady=14)

def get_data():
    """Collect all inputs — plug your backend call here."""
    data = {
        "student_id":   entry_id.get(),
        "student_name": entry_name.get(),
        "attendance":   entries["Attendance (%)"].get(),
        "study_hours":  entries["Study Hours (per day)"].get(),
        "internal":     entries["Internal Marks (%)"].get(),
        "assignment":   entries["Assignment (%)"].get(),
        "prev_score":   entries["Previous Score (%)"].get(),
    }
    print(data)  # replace with: response = requests.post("http://localhost:5000/predict", json=data)

def clear():
    entry_id.delete(0, "end")
    entry_name.delete(0, "end")
    for e in entries.values():
        e.delete(0, "end")
    lbl_pred.config(text="")
    lbl_risk.config(text="")
    txt_rec.config(state="normal")
    txt_rec.delete("1.0", "end")
    txt_rec.config(state="disabled")

tk.Button(btn_frame, text="Predict Performance",
          bg="#3498db", fg="white", font=("Arial", 10, "bold"),
          padx=12, pady=6, relief="flat", command=get_data
          ).grid(row=0, column=0, padx=8)

tk.Button(btn_frame, text="Clear",
          bg="#e67e22", fg="white", font=("Arial", 10, "bold"),
          padx=12, pady=6, relief="flat", command=clear
          ).grid(row=0, column=1, padx=8)

tk.Button(btn_frame, text="Exit",
          bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
          padx=12, pady=6, relief="flat", command=root.destroy
          ).grid(row=0, column=2, padx=8)

# ── result frame ──────────────────────────────────────────────────────────────
res = tk.LabelFrame(root, text="Prediction Results",
                    font=("Arial", 10, "bold"), bg="#f0f2f5", fg="#2c3e50",
                    padx=14, pady=10)
res.pack(fill="x", padx=20, pady=(0, 16))

tk.Label(res, text="Prediction:",     bg="#f0f2f5").grid(row=0, column=0, sticky="w", pady=3)
tk.Label(res, text="Risk Level:",     bg="#f0f2f5").grid(row=1, column=0, sticky="w", pady=3)
tk.Label(res, text="Recommendation:", bg="#f0f2f5").grid(row=2, column=0, sticky="nw", pady=3)

lbl_pred = tk.Label(res, text="", bg="#f0f2f5", font=("Arial", 10, "bold"))
lbl_risk = tk.Label(res, text="", bg="#f0f2f5", font=("Arial", 10, "bold"))
txt_rec  = tk.Text(res, height=2, width=52, state="disabled",
                   bg="white", relief="flat", wrap="word")

lbl_pred.grid(row=0, column=1, sticky="w", padx=10)
lbl_risk.grid(row=1, column=1, sticky="w", padx=10)
txt_rec .grid(row=2, column=1, sticky="w", padx=10)

res.columnconfigure(1, weight=1)

root.mainloop()
