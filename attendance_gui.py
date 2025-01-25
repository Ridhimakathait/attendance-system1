import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from recognize import recognize_face, log_attendance
import sqlite3

class AttendanceSystemGUI:
    def __init__(self, master):
        self.master = master
        master.title("Attendance System")

        self.label = tk.Label(master, text="Upload Image for Recognition")
        self.label.pack()

        self.upload_button = tk.Button(master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.recognize_button = tk.Button(master, text="Recognize", command=self.recognize_face)
        self.recognize_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.attendance_button = tk.Button(master, text="Log Attendance", command=self.log_attendance)
        self.attendance_button.pack()

        self.display_button = tk.Button(master, text="Display Attendance Records", command=self.display_records)
        self.display_button.pack()

        self.records_tree = ttk.Treeview(master, columns=("ID", "Name", "Timestamp"), show='headings')
        self.records_tree.heading("ID", text="ID")
        self.records_tree.heading("Name", text="Name")
        self.records_tree.heading("Timestamp", text="Timestamp")
        self.records_tree.pack()

    def upload_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.image_name = self.image_path.split("/")[-2]  
            self.result_label.config(text=f"Image uploaded: {self.image_name}")

    def recognize_face(self):
        if hasattr(self, 'image_path'):
            recognized_name, accuracy = recognize_face(self.image_path)  
            if recognized_name:
                self.result_label.config(text=f"Recognized: {recognized_name}, Accuracy: {accuracy:.2f}%")  
                self.recognized_name = recognized_name  
            else:
                self.result_label.config(text="Face not recognized or low accuracy.")
        else:
            messagebox.showwarning("Warning", "Please upload an image first.")

    def log_attendance(self):
        if hasattr(self, 'recognized_name'):
            log_attendance(self.recognized_name)
            messagebox.showinfo("Success", f"Attendance logged for {self.recognized_name}.")
        else:
            messagebox.showwarning("Warning", "No recognized name to log.")

    def display_records(self):
        
        for record in self.records_tree.get_children():
            self.records_tree.delete(record)

        
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM attendance")
        records = cursor.fetchall()
        conn.close()

        
        for record in records:
            self.records_tree.insert("", tk.END, values=record)

if __name__ == "__main__":
    root = tk.Tk()
    gui = AttendanceSystemGUI(root)
    root.mainloop()
