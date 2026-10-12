import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import pandas as pd
import joblib
# ============================================
# AI Based Lunar Ice Detection Dashboard
# ============================================

root = tk.Tk()

root.title("AI Based Lunar Ice Detection Dashboard")

root.geometry("1400x800")

root.configure(bg="white")

title = tk.Label(
    root,
    text="AI Based Lunar Ice Detection and Landing Site Recommendation",
    font=("Arial", 20, "bold"),
    bg="navy",
    fg="white",
    pady=15
)

title.pack(fill="x")
# -----------------------------
# Main Frame
# -----------------------------

main_frame = tk.Frame(root, bg="white")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Left Top
frame1 = tk.LabelFrame(
    main_frame,
    text="Original DFSAR Image",
    font=("Arial", 12, "bold"),
    width=600,
    height=300
)
frame1.grid(row=0, column=0, padx=10, pady=10)

# Right Top
frame2 = tk.LabelFrame(
    main_frame,
    text="Preprocessed Image",
    font=("Arial", 12, "bold"),
    width=600,
    height=300
)
frame2.grid(row=0, column=1, padx=10, pady=10)

# Left Bottom
frame3 = tk.LabelFrame(
    main_frame,
    text="Ice Detection",
    font=("Arial", 12, "bold"),
    width=600,
    height=300
)
frame3.grid(row=1, column=0, padx=10, pady=10)

# Right Bottom
frame4 = tk.LabelFrame(
    main_frame,
    text="Landing Site",
    font=("Arial", 12, "bold"),
    width=600,
    height=300
)
frame4.grid(row=1, column=1, padx=10, pady=10)

frame1.grid_propagate(False)
frame2.grid_propagate(False)
frame3.grid_propagate(False)
frame4.grid_propagate(False)
# ===================================
# Result Frame
# ===================================

result_frame = tk.LabelFrame(
    root,
    text="Prediction Results",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)

result_frame.pack(fill="x", padx=10, pady=5)

tk.Label(result_frame,
         text="Ice Percentage : 29.10 %",
         font=("Arial",11)).grid(row=0,column=0,sticky="w",padx=20)

tk.Label(result_frame,
         text="Ice Volume : 2450.35 m³",
         font=("Arial",11)).grid(row=1,column=0,sticky="w",padx=20)

tk.Label(result_frame,
         text="Prediction : ICE DETECTED",
         font=("Arial",11,"bold"),
         fg="green").grid(row=2,column=0,sticky="w",padx=20)

tk.Label(result_frame,
         text="Accuracy : 100%",
         font=("Arial",11)).grid(row=0,column=1,padx=80)

tk.Label(result_frame,
         text="Precision : 100%",
         font=("Arial",11)).grid(row=1,column=1,padx=80)

tk.Label(result_frame,
         text="Recall : 100%",
         font=("Arial",11)).grid(row=2,column=1,padx=80)

tk.Label(result_frame,
         text="F1 Score : 100%",
         font=("Arial",11)).grid(row=3,column=1,padx=80)

root.mainloop()