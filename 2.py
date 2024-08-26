#para instalar tkinter sebes colocar esto en el terminal:
# pip install tk
import tkinter as tk
from datetime import datetime

def actualizar_hora():
    ahora = datetime.now()
    hora_actual = ahora.strftime("%H:%M:%S")
    label.config(text=hora_actual)
    label.after(1000, actualizar_hora)

ventana = tk.Tk()
ventana.title("Reloj Digital")

label = tk.Label(ventana, font=("Arial", 72), bg="black", fg="green")
label.pack(pady=100)

actualizar_hora()

ventana.mainloop()