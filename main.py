import os, platform
import customtkinter as ctk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename(title="Text Converter - Exporter")
    file_path_entry.delete(0, 'end')
    file_path_entry.insert(0, file_path)
    print(file_path)

def rename_file():
    file_path = file_path_entry.get()
    with open(file_path, mode="r", encoding='utf-8') as f:
        lines = f.readlines()
    with open(file_path, mode="w", encoding='utf-8') as f:
        for line in lines:
            new_line = line.strip().replace(" ", "_").lower()
            if new_line != line.strip():
                f.write(new_line + "\n")
                print(f"{line.strip()} --> {new_line}")
            else:
                f.write(line)
    print("Done!")
    done_label = ctk.CTkLabel(root, text="Done!")
    done_label.place(relx=0.5, rely=0.5, anchor="center")
    root.after(2000, done_label.destroy)

def on_focus_in(event):
    if file_path_entry.get() == "path/to/file":
        file_path_entry.delete(0, ctk.END)
    current_mode = ctk.get_appearance_mode()
    if current_mode == 'Dark':
        file_path_entry.configure(text_color="white")
    elif current_mode == 'Light':
        file_path_entry.configure(text_color="black")

def on_focus_out(event):
    if file_path_entry.get() == "":
        file_path_entry.insert(0, "path/to/file")
        file_path_entry.configure(text_color="grey")

# Root Frame
root = ctk.CTk()
if platform.system() == 'Windows':
    root.iconbitmap(os.path.join('resources', 'icon.ico'))
root.title("File Renamer")
root.geometry("960x540")
root.resizable(False, False)

ctk.set_appearance_mode("dark")

# Directory Frame
dir_frame = ctk.CTkFrame(root)
dir_frame.pack(anchor="center", side="top", padx=10, pady=10)

file_path_label = ctk.CTkLabel(dir_frame, text="Enter file path:")
file_path_label.pack(side="left", padx=10, pady=10)

file_path_entry = ctk.CTkEntry(dir_frame)#, justify="center")
file_path_entry.insert(0, "path/to/file")
file_path_entry.configure(text_color="grey")
file_path_entry.bind("<FocusIn>", on_focus_in)
file_path_entry.bind("<FocusOut>", on_focus_out)
file_path_entry.pack(side="left", padx=10, pady=10)

browse_button = ctk.CTkButton(dir_frame, text="Browse", command=browse_file)
browse_button.pack(side="left", padx=10, pady=10)

# Button Frame
button_frame = ctk.CTkFrame(root)
button_frame.pack(side="bottom", padx=10, pady=10)

rename_button = ctk.CTkButton(button_frame, text="Rename Files", command=rename_file)
rename_button.pack(side="left", padx=10, pady=10)

root.mainloop()