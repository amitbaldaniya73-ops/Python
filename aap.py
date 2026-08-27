import tkinter as tk

app = tk.Tk()
app.title("My First App")
app.geometry("400x300")

label = tk.Label(app, text="Hello Python!", font=("Arial", 20))
label.pack(pady=50)

button = tk.Button(app, text="Click Me")
button.pack()

app.mainloop()
