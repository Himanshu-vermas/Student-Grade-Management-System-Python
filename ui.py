import tkinter as tk
from tkinter import messagebox

student_grades = {}

# ---------------- Functions ---------------- #

def add_student():
    name = name_entry.get()
    grade = grade_entry.get()

    if name == "" or grade == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    student_grades[name] = grade
    messagebox.showinfo("Success", f"{name} added successfully")
    clear_fields()
    display_students()


def update_student():
    name = name_entry.get()
    grade = grade_entry.get()

    if name in student_grades:
        student_grades[name] = grade
        messagebox.showinfo("Updated", f"{name}'s grade updated")
    else:
        messagebox.showerror("Error", "Student not found")

    clear_fields()
    display_students()


def delete_student():
    name = name_entry.get()

    if name in student_grades:
        del student_grades[name]
        messagebox.showinfo("Deleted", f"{name} deleted")
    else:
        messagebox.showerror("Error", "Student not found")

    clear_fields()
    display_students()


def display_students():
    text_area.delete(1.0, tk.END)

    if student_grades:
        text_area.insert(tk.END, "Student Name\tGrade\n")
        text_area.insert(tk.END, "-" * 30 + "\n")

        for name, grade in student_grades.items():
            text_area.insert(tk.END, f"{name}\t{grade}\n")
    else:
        text_area.insert(tk.END, "No Students Found")


def clear_fields():
    name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Student Grade Management System")
root.geometry("500x500")
root.configure(bg="#E8F6F3")

title = tk.Label(
    root,
    text="Student Grade Management System",
    font=("Arial", 16, "bold"),
    bg="#1ABC9C",
    fg="white",
    pady=10,
)
title.pack(fill="x")

frame = tk.Frame(root, bg="#E8F6F3")
frame.pack(pady=20)

tk.Label(frame, text="Student Name", bg="#E8F6F3", font=("Arial", 11)).grid(row=0, column=0, pady=8)

name_entry = tk.Entry(frame, font=("Arial", 11), width=25)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Grade", bg="#E8F6F3", font=("Arial", 11)).grid(row=1, column=0, pady=8)

grade_entry = tk.Entry(frame, font=("Arial", 11), width=25)
grade_entry.grid(row=1, column=1)

btn_frame = tk.Frame(root, bg="#E8F6F3")
btn_frame.pack()

tk.Button(btn_frame, text="Add", width=10, bg="green", fg="white", command=add_student).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Update", width=10, bg="blue", fg="white", command=update_student).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete", width=10, bg="red", fg="white", command=delete_student).grid(row=0, column=2, padx=5)

tk.Button(btn_frame, text="View", width=10, bg="orange", fg="white", command=display_students).grid(row=0, column=3, padx=5)

text_area = tk.Text(root, width=50, height=15, font=("Consolas", 11))
text_area.pack(pady=20)

root.mainloop()