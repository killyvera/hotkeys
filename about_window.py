import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import webbrowser

class AboutWindow:
    def __init__(self, parent, about_message, repo_link):
        self.parent = parent
        self.about_message = about_message
        self.repo_link = repo_link
        self.setup_ui()

    def setup_ui(self):
        self.parent.title("About")
        self.parent.geometry('400x300')

        # Agregar icono a la ventana (sin afectar la barra de tareas)
        icon_path = 'hotkeys_black.ico'
        self.parent.wm_iconbitmap(os.path.join(os.path.dirname(__file__), icon_path))

        # Crear un frame para contener la imagen y el texto
        content_frame = tk.Frame(self.parent)
        content_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Cargar la imagen
        logo_path = os.path.join(os.path.dirname(__file__), 'hotkeys_black.png')
        logo_image = Image.open(logo_path)
        logo_photo = ImageTk.PhotoImage(logo_image)

        # Label para mostrar la imagen
        image_label = tk.Label(content_frame, image=logo_photo)
        image_label.image = logo_photo  # Mantener una referencia para evitar que la imagen sea recolectada por el garbage collector
        image_label.pack(side=tk.TOP, pady=10)

        # Label para mostrar el mensaje de "Acerca de"
        message_label = tk.Label(content_frame, text=self.about_message, wraplength=380, justify=tk.LEFT)
        message_label.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx=0, pady=10)

        # Label para mostrar el enlace al repositorio
        link_label = tk.Label(content_frame, text="GitHub Repository", fg="purple", cursor="hand2")
        link_label.pack(side=tk.TOP, padx=0, pady=(0, 0))  # Ajuste del padding

        link_label.bind("<Button-1>", self.open_repo_link)

        # Botón para cerrar la ventana
        close_button = tk.Button(self.parent, text="Close", command=self.parent.destroy)
        close_button.pack(pady=(0, 20))  # Ajuste del padding

    def open_repo_link(self, event):
        webbrowser.open_new(self.repo_link)

def show_about_window(about_message, repo_link):
    root = tk.Tk()
    about_window = AboutWindow(root, about_message, repo_link)
    root.mainloop()

# Ejemplo de uso
if __name__ == "__main__":
    about_message = "Hotkeys Application\nVersion 1.0\n\nDeveloped by Your Name\n\n"
    repo_link = "https://github.com/your-repo-link"
    show_about_window(about_message, repo_link)
