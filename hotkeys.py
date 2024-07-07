import keyboard
import sys
import os
import pystray
from PIL import Image
import json

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
            "1": "{"+"}",
            "2": "<></>",
            "3": "<img src=\"\" >",
            "4": "[]",
            "5": "()",
            "6": "{"+"}",
            "7": "()",
            "8": "<span></span>",
            "9": "<p></p>",
            "0": "<>"
        }
        with open(file_path, 'w') as f:
            json.dump(default_snippets, f, indent=4)
        return default_snippets

    with open(file_path, 'r') as f:
        return json.load(f)

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

# Configurar hotkeys para cada snippet HTML con Ctrl+Alt+Tecla numérica
for key, snippet in html_snippets.items():
    keyboard.add_hotkey(f'ctrl+alt+{key}', insert_html_snippet, args=(snippet,))

# Configuración de la bandeja del sistema con pystray
if __name__ == '__main__':
    # Ocultar la consola de comandos
    # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    # Configuración del ícono en la bandeja del sistema
    try:
        icon_path = os.path.join(os.path.dirname(__file__), 'hotkeys.ico')
        icon = pystray.Icon("hotkeys")
        icon.icon = Image.open(icon_path)
        icon.title = "HTML Snippets"
        icon.menu = pystray.Menu(pystray.MenuItem("Quit", on_quit))
        icon.run()
    except KeyboardInterrupt:
        sys.exit(0)
