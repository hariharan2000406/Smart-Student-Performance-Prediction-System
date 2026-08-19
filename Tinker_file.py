import tkinter as tk
from tkinter import messagebox

# ── prediction logic ──────────────────────────────────────────────────────────
def predict(attendance, study_hours, internal_marks, assignment, prev_score):
    score = (
        attendance      * 0.25 +
        (study_hours / 10) * 100 * 0.15 +
        internal_marks  * 0.25 +
        assignment      * 0.15 +
        prev_score      * 0.20
    )

    if score >= 75:
        prediction = "Excellent Performance"
        risk       = "Low Risk"
        rec        = "Keep it up! Aim for distinction."
    elif score >= 60:
        prediction = "Good Performance"
        risk       = "Moderate Risk"
        rec        = "Focus on weak subjects and revise regularly."
    elif score >= 45:
        prediction = "Average Performance"
        risk       = "High Risk"
        rec        = "Attend extra classes and increase study hours."
    else:
        prediction = "Poor Performance"
        risk       = "Very High Risk"
        rec        = "Urgent: seek faculty help and improve attendance."

    return prediction, risk, rec

# ── main window ───────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Smart Student Performance Prediction System")
root.geometry("700x520")
root.resizable(False, False)
root.configure(bg="#f0f2f5")

# ── header frame ──────────────────────────────────────────────────────────────
header_frame = tk.Frame(root, bg="#2c3e50", pady=12)
header_frame.pack(fill="x")

tk.Label(
    header_frame,
    text="SMART STUDENT PERFORMANCE\nPREDICTION SYSTEM",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#2c3e50",
    justify="center"
).pack()

# ── content area ──────────────────────────────────────────────────────────────
content = tk.Frame(root, bg="#f0f2f5")
content.pack(fill="both", expand=True, padx=20, pady=10)

# ── student information frame ─────────────────────────────────────────────────
stu_frame = tk.LabelFrame(content, text="Student Information",
                          font=("Arial", 10, "bold"), bg="#f0f2f5",
                          fg="#2c3e50", padx=10, pady=10)
stu_frame.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="nsew")

tk.Label(stu_frame, text="Student ID",   bg="#f0f2f5").grid(row=0, column=0, sticky="w", pady=4)
tk.Label(stu_frame, text="Student Name", bg="#f0f2f5").grid(row=1, column=0, sticky="w", pady=4)

entry_id   = tk.Entry(stu_frame, width=22)
entry_name = tk.Entry(stu_frame, width=22)
entry_id  .grid(row=0, column=1, padx=8)
entry_name.grid(row=1, column=1, padx=8)

# ── academic information frame ────────────────────────────────────────────────
acad_frame = tk.LabelFrame(content, text="Academic Information",
                           font=("Arial", 10, "bold"), bg="#f0f2f5",
                           fg="#2c3e50", padx=10, pady=10)
acad_frame.grid(row=0, column=1, pady=5, sticky="nsew")

fields = [
    ("Attendance (%)",        "0–100"),
    ("Study Hours (per day)", "0–10"),
    ("Internal Marks (%)",    "0–100"),
    ("Assignment (%)",        "0–100"),
    ("Previous Score (%)",    "0–100"),
]

acad_entries = {}
for i, (label, hint) in enumerate(fields):
    tk.Label(acad_frame, text=label, bg="#f0f2f5").grid(row=i, column=0, sticky="w", pady=3)
    e = tk.Entry(acad_frame, width=18)
    e.grid(row=i, column=1, padx=8)
    acad_entries[label] = e

content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)

# ── action frame ──────────────────────────────────────────────────────────────
action_frame = tk.Frame(root, bg="#f0f2f5")
action_frame.pack(pady=6)

def on_predict():
    try:
        att   = float(acad_entries["Attendance (%)"].get())
        hrs   = float(acad_entries["Study Hours (per day)"].get())
        intm  = float(acad_entries["Internal Marks (%)"].get())
        asgn  = float(acad_entries["Assignment (%)"].get())
        prev  = float(acad_entries["Previous Score (%)"].get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all academic fields.")
        return

    pred, risk, rec = predict(att, hrs, intm, asgn, prev)
    lbl_pred.config(text=pred)
    lbl_risk.config(text=risk,
                    fg="#e74c3c" if "High" in risk else "#27ae60")
    txt_rec.config(state="normal")
    txt_rec.delete("1.0", "end")
    txt_rec.insert("1.0", rec)
    txt_rec.config(state="disabled")

def on_clear():
    entry_id.delete(0, "end")
    entry_name.delete(0, "end")
    for e in acad_entries.values():
        e.delete(0, "end")
    lbl_pred.config(text="")
    lbl_risk.config(text="", fg="#2c3e50")
    txt_rec.config(state="normal")
    txt_rec.delete("1.0", "end")
    txt_rec.config(state="disabled")

tk.Button(action_frame, text="📊  Predict Performance",
          bg="#3498db", fg="white", font=("Arial", 10, "bold"),
          padx=12, pady=6, relief="flat", command=on_predict
          ).grid(row=0, column=0, padx=8)

tk.Button(action_frame, text="○  Clear",
          bg="#e67e22", fg="white", font=("Arial", 10, "bold"),
          padx=12, pady=6, relief="flat", command=on_clear
          ).grid(row=0, column=1, padx=8)

tk.Button(action_frame, text="✕  Exit",
          bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
          padx=12, pady=6, relief="flat", command=root.destroy
          ).grid(row=0, column=2, padx=8)

# ── result frame ──────────────────────────────────────────────────────────────
result_frame = tk.LabelFrame(root, text="Prediction Results",
                             font=("Arial", 10, "bold"), bg="#f0f2f5",
                             fg="#2c3e50", padx=14, pady=10)
result_frame.pack(fill="x", padx=20, pady=(4, 14))

tk.Label(result_frame, text="Prediction:",    bg="#f0f2f5", anchor="w").grid(row=0, column=0, sticky="w", pady=3)
tk.Label(result_frame, text="Risk Level:",    bg="#f0f2f5", anchor="w").grid(row=1, column=0, sticky="w", pady=3)
tk.Label(result_frame, text="Recommendation:",bg="#f0f2f5", anchor="w").grid(row=2, column=0, sticky="nw", pady=3)

lbl_pred = tk.Label(result_frame, text="", bg="#f0f2f5", font=("Arial", 10, "bold"), fg="#2c3e50")
lbl_risk = tk.Label(result_frame, text="", bg="#f0f2f5", font=("Arial", 10, "bold"))

lbl_pred.grid(row=0, column=1, sticky="w", padx=10)
lbl_risk.grid(row=1, column=1, sticky="w", padx=10)

txt_rec = tk.Text(result_frame, height=2, width=55, state="disabled",
                  bg="#ffffff", relief="flat", wrap="word")
txt_rec.grid(row=2, column=1, sticky="w", padx=10)

result_frame.columnconfigure(1, weight=1)

# ── run ───────────────────────────────────────────────────────────────────────
root.mainloop()
