import tkinter as tk
from tkinter import messagebox
import os

class AboutWindow:
    def __init__(self, parent, about_message):
        self.parent = parent
        self.about_message = about_message
        self.setup_ui()

    def setup_ui(self):
        self.parent.title("About")
        self.parent.geometry('300x200')

        # Agregar icono a la ventana (sin afectar la barra de tareas)
        icon_path = 'hotkeys_black.ico'
        self.parent.wm_iconbitmap(os.path.join(os.path.dirname(__file__), 'hotkeys_black.ico'))

        # Label para mostrar el mensaje de "Acerca de"
        message_label = tk.Label(self.parent, text=self.about_message, wraplength=280, justify=tk.LEFT)
        message_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Botón para cerrar la ventana
        close_button = tk.Button(self.parent, text="Close", command=self.parent.destroy)
        close_button.pack(pady=10)

def show_about_window(about_message):
    root = tk.Tk()
    about_window = AboutWindow(root, about_message)
    root.mainloop()

# Ejemplo de uso
# if __name__ == "__main__":
#     show_about_window("This is a customizable About message. You can put any information here.")
