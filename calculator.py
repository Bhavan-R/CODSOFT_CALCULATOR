import tkinter as tk

# Function to handle button clicks
def click(event):
    button = event.widget.cget("text")

    if button == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except:
            screen_var.set("Error")

    elif button == "C":
        screen_var.set("")

    elif button == "⌫":
        current = screen.get()
        screen_var.set(current[:-1])

    else:
        screen_var.set(screen.get() + button)


# Main Window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("430x700")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Screen Variable
screen_var = tk.StringVar()

# Display Screen
screen = tk.Entry(
    root,
    textvar=screen_var,
    font=("Arial", 30, "bold"),
    bd=10,
    relief=tk.FLAT,
    justify=tk.RIGHT,
    bg="white",
    fg="black"
)

screen.pack(fill="x", padx=15, pady=20, ipady=20)

# Buttons Frame
buttons_frame = tk.Frame(root, bg="#1e1e2f")
buttons_frame.pack()

# Button Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Button Colors
colors = {
    "/": "#ff9800",
    "*": "#ff9800",
    "-": "#ff9800",
    "+": "#ff9800",
    "=": "#4caf50",
    "C": "#f44336"
}

# Create Main Buttons
for row in buttons:
    frame = tk.Frame(buttons_frame, bg="#1e1e2f")
    frame.pack(pady=5)

    for text in row:
        bg_color = colors.get(text, "#2d89ef")

        btn = tk.Button(
            frame,
            text=text,
            font=("Arial", 22, "bold"),
            width=5,
            height=2,
            bg=bg_color,
            fg="white",
            activebackground="#555",
            activeforeground="white",
            relief=tk.RAISED,
            bd=4,
            cursor="hand2"
        )

        btn.pack(side=tk.LEFT, padx=6, pady=6)
        btn.bind("<Button-1>", click)

# Single Delete Button
delete_btn = tk.Button(
    root,
    text="⌫",
    font=("Arial", 24, "bold"),
    width=18,
    height=2,
    bg="#9c27b0",
    fg="white",
    activebackground="#7b1fa2",
    activeforeground="white",
    relief=tk.RAISED,
    bd=4,
    cursor="hand2"
)

delete_btn.pack(pady=15)
delete_btn.bind("<Button-1>", click)

# Run App
root.mainloop()