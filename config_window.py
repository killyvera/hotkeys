import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os

class ConfigWindow:
    def __init__(self, parent, html_snippets, snippets_file):
        self.parent = parent
        self.html_snippets = html_snippets
        self.snippets_file = snippets_file
        self.setup_ui()

    def setup_ui(self):
        self.parent.title("hotkeys Config")
        self.parent.geometry('400x300')

        icon_path = 'hotkeys_black.ico'
        self.parent.wm_iconbitmap(os.path.join(os.path.dirname(__file__), 'hotkeys_black.ico'))

        # Crear una tabla (Treeview) para mostrar los snippets y shortcuts
        self.tree = ttk.Treeview(self.parent, columns=('Snippet'))
        self.tree.heading('#0', text='Shortcut')
        self.tree.heading('#1', text='Snippet')

        # Cargar datos en la tabla
        self.refresh_table()

        # Configurar evento de doble clic para editar el snippet
        self.tree.bind("<Double-1>", self.edit_snippet)

        self.tree.pack(expand=True, fill=tk.BOTH)

        # Botón para guardar cambios
        save_button = ttk.Button(self.parent, text="Save", command=self.save_changes)
        save_button.pack(pady=10)

    def refresh_table(self):
        # Limpiar la tabla antes de cargar los datos actualizados
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Cargar datos actualizados en la tabla
        for key, snippet in self.html_snippets.items():
            self.tree.insert('', 'end', text=key, values=(snippet,))

    def edit_snippet(self, event):
        item = self.tree.selection()[0]
        key = self.tree.item(item, 'text')
        current_snippet = self.tree.item(item, 'values')[0]

        new_snippet = simpledialog.askstring("Edit hotkey", f"add new value to {key}:", initialvalue=current_snippet)

        if new_snippet is not None:
            self.tree.set(item, '#1', new_snippet)

    def save_changes(self):
        # Guardar los cambios en el archivo JSON
        new_snippets = {}
        for item in self.tree.get_children():
            key = self.tree.item(item)['text']
            snippet = self.tree.item(item)['values'][0]
            new_snippets[key] = snippet

        try:
            with open(self.snippets_file, 'w') as f:
                json.dump(new_snippets, f, indent=4)
            # messagebox.showinfo("Guardado", "Cambios guardados correctamente.")

            # Actualizar los snippets en la interfaz después de guardar
            self.html_snippets = new_snippets
            self.refresh_table()

            # Configurar nuevamente los hotkeys con los snippets actualizados
            from main import configure_hotkeys
            configure_hotkeys(new_snippets)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los cambios: {str(e)}")

def show_config_window(html_snippets, snippets_file):
    root = tk.Tk()
    config_window = ConfigWindow(root, html_snippets, snippets_file)
    root.mainloop()

    return config_window.html_snippets
