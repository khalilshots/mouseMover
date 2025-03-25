import tkinter as tk
import pyautogui
import random

# Flag to control whether mouse movement is active
running = False

# Moves the mouse randomly every second if running is True
def move_mouse():
    if running:
        x = random.randint(900, 1500)
        y = random.randint(400, 800)
        pyautogui.moveTo(x, y, duration=0.2)
        root.after(1000, move_mouse)  # Schedule next move in 1 second

# Starts the mouse movement
def start():
    global running
    if not running:
        print("Starting mouse movement...")
        running = True
        move_mouse()

# Stops the mouse movement (triggered by pressing X)
def stop(event=None):
    global running
    print("Stopping mouse movement via 'X' key...")
    running = False

# Set up the GUI window
root = tk.Tk()
root.title("Mouse Mover")
root.geometry("300x180")

# 📌 Header label that shows instructions
header_label = tk.Label(
    root,
    text="Press 'X' on your keyboard to stop",
    font=("Arial", 15),
    fg="white"
)
header_label.pack(pady=(15, 5))  # Top padding: 15px, bottom: 5px

# 🟢 Start Button
start_btn = tk.Button(
    root,
    text="Start",
    command=start,
    bg="green",
    fg="white",
    font=("Arial", 12)
)
start_btn.pack(pady=20)

# 🧠 Bind the X key (lowercase and uppercase) to the stop function
root.bind("<KeyPress-x>", stop)
root.bind("<KeyPress-X>", stop)

# 🔓 Make sure window can receive keyboard input
root.focus_set()

# Start the GUI event loop
root.mainloop()
