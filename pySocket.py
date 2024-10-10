import socket
import random
import time

def simular_gpio():
  # Simula cambios aleatorios en los estados de los GPIOs
  return [random.randint(0, 1) for _ in range(4)]

# Configuración del socket
HOST = '192.168.0.17'
PORT = 4040

while True:
  # Crear un socket TCP/IP
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
      s.connect((HOST, PORT))
      print(f"Conectado a {HOST}:{PORT}")

      # Simular lectura de GPIOs
      estados_gpio = simular_gpio()
      # Convertir a bytes
      datos = bytes(estados_gpio)
      # Enviar datos
      s.sendall(datos)
      print(f"Datos enviados: {datos}")

    except Exception as e:
      print(f"Ocurrió un error: {e}")

  print("Socket cerrado")
  time.sleep(1)  # Esperar 1 segundo antes de volver a conectar