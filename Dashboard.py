"""
Dashboard de Programación Orientada a Objetos
Autora: Mercy Katherine Amaya
Curso: Programación Orientada a Objetos
Versión: 1.0
Año: 2026
Descripción:
Este dashboard permite navegar por las unidades del curso,
visualizar scripts en Python y ejecutarlos desde un menú interactivo.
"""

import os
import subprocess


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Mostrando código del script: {os.path.basename(ruta_script)} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("❌ El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"❌ Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"❌ Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    print("Bienvenida/o al Dashboard de Programación Orientada a Objetos")
    print("Autora: Mercy Katherine Amaya")
    print("Curso: Programación Orientada a Objetos\n")

    unidades = {
        '1': 'Unidad 1 - Introducción a POO',
        '2': 'Unidad 2 - Clases y Objetos'
    }

    while True:
        print("\n=== Dashboard POO - Mercy Katherine Amaya ===")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")

        if eleccion_unidad == '0':
            print("Gracias por usar el Dashboard POO de Mercy Katherine Amaya. ¡Hasta pronto!")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("❌ Opción no válida. Por favor, intenta de nuevo.")


def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\n📂 Submenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")

        if eleccion_carpeta == '0':
            break
        else:
            try:
                indice = int(eleccion_carpeta) - 1
                if 0 <= indice < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
                else:
                    print("❌ Opción no válida.")
            except ValueError:
                print("❌ Ingresa un número válido.")


def mostrar_scripts(ruta_sub_carpeta):
    scripts = [
        f.name for f in os.scandir(ruta_sub_carpeta)
        if f.is_file() and f.name.endswith('.py')
    ]

    while True:
        print("\n🐍 Scripts disponibles")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script: ")

        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                indice = int(eleccion_script) - 1
                if 0 <= indice < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                    codigo = mostrar_codigo(ruta_script)

                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            print("▶ Ejecutando el script seleccionado...")
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("ℹ No se ejecutó el script.")
                        else:
                            print("❌ Opción no válida.")

                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("❌ Opción no válida.")
            except ValueError:
                print("❌ Ingresa un número válido.")


# Punto de entrada del programa
if __name__ == "__main__":
    mostrar_menu()

