import keyboard
import sys
from pynput.keyboard import Key, Listener

def main():
    # Mapeo de teclas numéricas del bloque numérico a etiquetas HTML
    html_snippets = {
        '1': '<h1></h1>',
        '2': '<div></div>',
        '3': '<img src="" >',
        '4': '<h4></h4>',
        '5': '()=>()',
        '6': '<h6></h6>',
        '7': '<div></div>',
        '8': '<span></span>',
        '9': '<p></p>',
        '0': '<section></section>'
    }

    # Función para manejar la inserción de snippets HTML
    def insert_html_snippet(tag):
        keyboard.write(tag)

    # Configurar los hotkeys para cada tecla numérica del bloque numérico con Ctrl + Alt
    for key, snippet in html_snippets.items():
        keyboard.add_hotkey(f'ctrl+alt+{key}', insert_html_snippet, args=(snippet,))

    print("Hotkeys configurados. Presiona Ctrl+Alt y la tecla numérica del bloque para insertar el snippet HTML correspondiente.")

    # Mantener el script en ejecución para escuchar los hotkeys
    keyboard.wait()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
