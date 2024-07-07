import keyboard
import sys
import os
import ctypes
import pystray
from PIL import Image

# Función para manejar la salida del programa
def on_quit(icon, item):
    icon.stop()
    sys.exit(0)

# Función para insertar un snippet HTML en el documento
def insert_html_snippet(tag):
    keyboard.write(tag)

# Configuración de snippets HTML para cada tecla numérica del bloque numérico
html_snippets = {
    '1': '{'+'}',
    '2': '<></>',
    '3': '<img src="" >',
    '4': '[]',
    '5': '()',
    '6': '{'+'}',
    '7': '()',
    '8': '<span></span>',
    '9': '<p></p>',
    '0': '<>'
}

# Configurar hotkeys para cada snippet HTML con Ctrl+Alt+Tecla numérica
for key, snippet in html_snippets.items():
    keyboard.add_hotkey(f'ctrl+alt+{key}', insert_html_snippet, args=(snippet,))

# Mensaje de configuración de hotkeys
print("Hotkeys configurados. Presiona Ctrl+Alt y la tecla numérica del bloque para insertar el snippet HTML correspondiente.")

# Configuración de la bandeja del sistema con pystray
if __name__ == '__main__':
    # Ocultar la consola de comandos
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

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
