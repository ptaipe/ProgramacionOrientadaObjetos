import subprocess
import time
import sys
import os

def run():
    # Rutas de tus archivos
    api_path = os.path.join("api", "app.py")
    app_path = os.path.join("CrudClientesProductoVentas", "main.py")

    print("Iniciando API Flask...")
    api_process = subprocess.Popen([sys.executable, api_path])

    # Espera breve para que la API levante
    time.sleep(2)

    print("Iniciando aplicación de consola...")
    app_process = subprocess.Popen([sys.executable, app_path])

    try:
        # Espera mientras la app de consola se ejecuta
        app_process.wait()
    except KeyboardInterrupt:
        print("\nCerrando procesos...")

    # Finaliza ambos procesos al salir
    api_process.terminate()
    app_process.terminate()

if __name__ == "__main__":
    run()