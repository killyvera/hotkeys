import keyboard
import sys
import os
import pystray
from PIL import Image
import json
from config_window import show_config_window

# Función para manejar la salida del programa
def on_quit(icon, item):
    icon.stop()
    sys.exit(0)

# Función para insertar un snippet HTML en el documento
def insert_html_snippet(tag):
    keyboard.write(tag)

# Función para cargar snippets desde un archivo JSON
def load_snippets(file_path):
    if not os.path.exists(file_path):
        # Si el archivo no existe, crear uno con contenido por defecto
        default_snippets = {
            "1": "def_1",
            "2": "def_2",
            "3": "def_3",
            "4": "def_4",
            "5": "def_5",
            "6": "def_6",
            "7": "def_7",
            "8": "def_8",
            "9": "def_9",
            "0": "def_0"
        }
        with open(file_path, 'w') as f:
            json.dump(default_snippets, f, indent=4)
        return default_snippets

    with open(file_path, 'r') as f:
        return json.load(f)

# Función para configurar las hotkeys con los snippets actuales
def configure_hotkeys(html_snippets):
    # Eliminar todas las hotkeys existentes antes de configurar las nuevas
    keyboard.unhook_all()

    # Configurar hotkeys para cada snippet HTML con Ctrl+Alt+Tecla numérica
    for key, snippet in html_snippets.items():
        keyboard.add_hotkey(f'ctrl+alt+{key}', insert_html_snippet, args=(snippet,))

# Función para mostrar la ventana de configuración y actualizar snippets
def show_config_window_and_update(html_snippets, snippets_file):
    updated_snippets = show_config_window(html_snippets, snippets_file)
    if updated_snippets:
        # Actualizar html_snippets con los snippets actualizados
        html_snippets.update(updated_snippets)
        # Reconfigurar hotkeys con los snippets actualizados
        configure_hotkeys(html_snippets)

# Obtener la ruta absoluta de AppData\Roaming para el archivo JSON
app_data_dir = os.path.expanduser(os.path.join('~', 'AppData', 'Roaming', 'hotkeys'))
print(f"Ruta de la carpeta hotkeys: {app_data_dir}")  # Imprimir la ruta antes de crear la carpeta

try:
    os.makedirs(app_data_dir, exist_ok=True)
except OSError as e:
    print(f"Error al crear la carpeta: {e}")

snippets_file = os.path.join(app_data_dir, 'snippets.json')

# Cargar snippets desde el archivo JSON
html_snippets = load_snippets(snippets_file)

# Configurar hotkeys inicialmente
configure_hotkeys(html_snippets)

# Configuración de la bandeja del sistema con pystray
if __name__ == '__main__':
    # Configuración del ícono en la bandeja del sistema
    try:
        icon_path = os.path.join(os.path.dirname(__file__), 'hotkeys.ico')
        icon = pystray.Icon("hotkeys")
        icon.icon = Image.open(icon_path)
        icon.title = "hotkeys Ver0.1"
        
        # Añadir opción de configuración al menú de la bandeja del sistema
        def open_config_window(icon, item):
            show_config_window_and_update(html_snippets, snippets_file)
        
        icon.menu = pystray.Menu(pystray.MenuItem("Configuración", open_config_window),
                                 pystray.MenuItem("Quit", on_quit))
        
        icon.run()
    except KeyboardInterrupt:
        sys.exit(0)
