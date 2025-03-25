import tkinter as tk
import pyautogui
import random

running = False

def move_mouse():
    if running:
        x = random.randint(900, 1500)
        y = random.randint(400, 800)
        pyautogui.moveTo(x, y, duration=0.2)
        root.after(1000, move_mouse)

def start():
    global running
    if not running:
        print("Starting mouse movement...")
        running = True
        move_mouse()

def stop():
    global running
    print("Stopping mouse movement...")
    running = False

# GUI Setup
root = tk.Tk()
root.title("Mouse Mover")
root.geometry("300x150")

start_btn = tk.Button(root, text="Start", command=start, bg="green", fg="white", font=("Arial", 12))
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Stop", command=stop, bg="red", fg="white", font=("Arial", 12))
stop_btn.pack(pady=10)

root.mainloop()
