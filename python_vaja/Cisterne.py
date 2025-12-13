import tkinter as tk
from tkinter import messagebox
import json
import os
import sys

# -----------------------------
# Paths for JSON file
# -----------------------------
# Get folder of script safely, even in IDEs
if getattr(sys, 'frozen', False):
    # If packaged as executable
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "inventory.json")

# -----------------------------
# Initialize inventory
# -----------------------------
# Default inventory if file doesn't exist
inventory = {f"T {i+1}": {"content": f"Content {i+1}", "volume": 0, "Dodatki": 0} for i in range(13)}

# -----------------------------
# Functions to load/save inventory
# -----------------------------
def save_inventory():
    try:
        with open(file_path, "w") as f:
            json.dump(inventory, f)
        print(f"Inventory saved to {file_path}!")
    except Exception as e:
        print("Error saving inventory:", e)

def load_inventory():
    global inventory
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                inventory = json.load(f)
            # Convert numeric fields to float
            for item in inventory.values():
                item["volume"] = float(item.get("volume", 0))
                item["Dodatki"] = (item.get("Dodatki", 0))
            print(f"Inventory loaded from {file_path}!")
        except Exception as e:
            print("Error loading inventory:", e)
    else:
        print("No saved inventory found, starting fresh.")

# Load inventory at start
load_inventory()

# -----------------------------
# Function to open sub-window
# -----------------------------
def open_item_window(item_name):
    sub_window = tk.Toplevel(root)
    sub_window.title(item_name)

    # -----------------------------
    # Center the sub-window
    # -----------------------------
    window_width = 300
    window_height = 300
    screen_width = sub_window.winfo_screenwidth()
    screen_height = sub_window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    sub_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    tk.Label(sub_window, text=f"{item_name} Details", font=("Arial", 16, "bold")).pack(pady=10)

    # Content
    tk.Label(sub_window, text="Content:").pack()
    content_entry = tk.Entry(sub_window, width=25)
    content_entry.insert(0, inventory[item_name]["content"])
    content_entry.pack(pady=5)

    # Volume
    tk.Label(sub_window, text="Volume (L):").pack()
    volume_entry = tk.Entry(sub_window, width=25)
    volume_entry.insert(0, str(inventory[item_name]["volume"]))
    volume_entry.pack(pady=5)

    # Dodatki
    tk.Label(sub_window, text="Dodatki:").pack()
    dodatki_entry = tk.Entry(sub_window, width=25)
    dodatki_entry.insert(0, str(inventory[item_name]["Dodatki"]))
    dodatki_entry.pack(pady=5)

    # Save button
    def save_changes():
        inventory[item_name]["content"] = content_entry.get()
        try:
            inventory[item_name]["volume"] = float(volume_entry.get())
            inventory[item_name]["Dodatki"] = (dodatki_entry.get())
            save_inventory()
            messagebox.showinfo("Saved", f"{item_name} updated successfully!")
            sub_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Volume and Dodatki must be numbers.")

    tk.Button(sub_window, text="Save", command=save_changes).pack(pady=10)

# -----------------------------
# Main window
# -----------------------------
root = tk.Tk()
root.title("Inventory Dashboard")

# -----------------------------
# Center the main window
# -----------------------------
root.update_idletasks()  # Update geometry info
window_width = 600
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

tk.Label(root, text="Inventory Dashboard", font=("Arial", 20, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=20)

# -----------------------------
# Create 13 rounded-like buttons
# -----------------------------
row, col = 0, 0
for name in inventory:
    canvas = tk.Canvas(frame, width=100, height=50, bg="white", highlightthickness=0)
    canvas.grid(row=row, column=col, padx=10, pady=10)

    r = 20
    canvas.create_oval(0, 0, r, r, fill="lightblue", outline="lightblue")
    canvas.create_oval(100-r, 0, 100, r, fill="lightblue", outline="lightblue")
    canvas.create_oval(0, 50-r, r, 50, fill="lightblue", outline="lightblue")
    canvas.create_oval(100-r, 50-r, 100, 50, fill="lightblue", outline="lightblue")
    canvas.create_rectangle(r/2, 0, 100-r/2, 50, fill="lightblue", outline="lightblue")
    canvas.create_rectangle(0, r/2, 100, 50-r/2, fill="lightblue", outline="lightblue")

    canvas.create_text(50, 25, text=name, font=("Arial", 10))

    # Lambda fix: default argument binds the current name
    canvas.bind("<Button-1>", lambda e, n=name: open_item_window(n))

    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()
