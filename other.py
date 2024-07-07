import tkinter as tk
from tkinter import ttk, messagebox
import json

class ConfigWindow:
    def __init__(self, parent, html_snippets, snippets_file):
        self.parent = parent
        self.html_snippets = html_snippets
        self.snippets_file = snippets_file
        self.setup_ui()

    def setup_ui(self):
        self.parent.title("Configuración de Snippets HTML")
        self.parent.geometry('400x300')

        # Crear una tabla (Treeview) para mostrar los snippets y shortcuts
        self.tree = ttk.Treeview(self.parent, columns=('Snippet'))
        self.tree.heading('#0', text='Shortcut')
        self.tree.heading('#1', text='Snippet')

        # Cargar datos en la tabla
        self.load_snippets_into_tree()

        self.tree.pack(expand=True, fill=tk.BOTH)

        # Botón para guardar cambios
        self.save_button = ttk.Button(self.parent, text="Guardar Cambios", command=self.save_changes)
        self.save_button.pack(pady=10)

        # Configurar evento de doble click para editar snippet
        self.tree.bind("<Double-1>", self.edit_snippet)

    def load_snippets_into_tree(self):
        # Limpiar árbol antes de cargar los datos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Cargar datos en la tabla
        for key, snippet in self.html_snippets.items():
            self.tree.insert('', 'end', text=key, values=(snippet))

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
            messagebox.showinfo("Guardado", "Cambios guardados correctamente.")

            # Actualizar html_snippets con los snippets actualizados
            self.html_snippets.update(new_snippets)
            # Actualizar la vista en la ventana de configuración
            self.load_snippets_into_tree()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los cambios: {str(e)}")

    def edit_snippet(self, event):
        # Obtener el ítem seleccionado en la tabla
        item = self.tree.selection()[0]
        key = self.tree.item(item, "text")
        current_snippet = self.tree.item(item, "values")[0]

        # Abrir ventana de edición de snippet
        edit_window = tk.Toplevel(self.parent)
        edit_window.title(f"Editar Snippet para '{key}'")

        # Campo de texto para editar el snippet
        snippet_var = tk.StringVar(value=current_snippet)
        snippet_entry = ttk.Entry(edit_window, textvariable=snippet_var, width=40)
        snippet_entry.pack(padx=10, pady=10)

        # Función para guardar el snippet editado
        def save_snippet():
            new_snippet = snippet_var.get()
            if new_snippet:
                self.tree.set(item, '#1', new_snippet)
                edit_window.destroy()
            else:
                messagebox.showwarning("Campo Vacío", "Por favor ingrese un snippet válido.")

        # Botón para guardar el snippet editado
        save_button = ttk.Button(edit_window, text="Guardar", command=save_snippet)
        save_button.pack(pady=10)

# Función para mostrar la ventana de configuración y actualizar snippets
def show_config_window_and_update(html_snippets, snippets_file):
    root = tk.Tk()
    config_window = ConfigWindow(root, html_snippets, snippets_file)
    root.mainloop()

    return config_window.html_snippets  # Devolver los snippets actualizados después de cerrar la ventana

# # Ejemplo de carga inicial y uso
# if __name__ == '__main__':
#     # Ejemplo de carga inicial de snippets (puedes cargarlos desde tu archivo JSON)
#     html_snippets = {
#         "1": "def_1",
#         "2": "def_2",
#         "3": "def_3",
#         "4": "def_4",
#         "5": "def_5"
#     }

#     snippets_file = "snippets.json"  # Nombre del archivo JSON (puedes ajustar esto según tu estructura)

#     updated_snippets = show_config_window_and_update(html_snippets, snippets_file)
#     if updated_snippets:
#         # Aquí podrías actualizar html_snippets en tu aplicación principal si fuera necesario
#         print("Snippets actualizados:", updated_snippets)