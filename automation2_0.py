import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_folder():
    folder_path = filedialog.askdirectory()

    if not folder_path:
        return

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"],
        "Audios": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        "PDFs": [".pdf"],
        "Docs": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
        "Code": [".py", ".java", ".cpp", ".js", ".html", ".css", ".php", ".rb", ".go"],
        "Archives": [".zip", ".rar", ".7z"],
        "Executables": [".exe", ".msi", ".bat", ".sh"]
    }

    moved = 0

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if not os.path.isfile(file_path) or file.startswith("."):
            continue

        if file == os.path.basename(__file__):
            continue

        matched_folder = "Others"

        for folder, extensions in file_types.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                matched_folder = folder
                break

        dest_folder = os.path.join(folder_path, matched_folder)
        os.makedirs(dest_folder, exist_ok=True)

        dest_path = os.path.join(dest_folder, file)

        if os.path.exists(dest_path):
            base, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(dest_path):
                dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
                counter += 1

        shutil.move(file_path, dest_path)
        moved += 1

    messagebox.showinfo("Done", f"Files organised successfully ✅\n{moved} file(s) moved.")


root = tk.Tk()
root.title("File Organizer")

btn = tk.Button(root, text="Select Folder & Organize", command=organize_folder, padx=20, pady=10)
btn.pack(pady=30)

root.mainloop()
