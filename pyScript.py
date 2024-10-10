import RPi.GPIO as GPIO
import socket
import time
import struct

# Configuración de los GPIOs
GPIO.setmode(GPIO.BCM)  # Numeración BCM
gpio_pins = [26, 5, 6, 13]  # Reemplazar con los pines conectados

# Configurar los pines GPIO
for pin in gpio_pins:
    GPIO.setup(pin, GPIO.IN)  # Configura el pin como entrada

# Configuración del socket
HOST = '192.168.0.17'  # Dirección IP del servidor
PORT = 4040            # Puerto del servidor

# Configuración de reintentos
max_retries = 3  # Número máximo de reintentos

# Identificador del dispositivo (4 bytes)
device_id = 12345  # Cambia este valor según tu necesidad

try:
    while True:
        # Crear un socket TCP/IP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((HOST, PORT))
                print(f"Conectado a {HOST}:{PORT}")

                # Almacenar la última lectura de los pines
                last_states = [GPIO.input(pin) for pin in gpio_pins]
                print(f"last_states: {last_states}") 

                # Enviar el estado inicial
                # Empaquetar el ID del dispositivo y los estados de los GPIOs
                data = struct.pack('I', device_id) + bytes(last_states)  # 'I' para un entero sin signo de 4 bytes
                s.sendall(data)
                print(f"Datos enviados (inicial): {data}")

                # Leer el estado de los GPIOs
                while True:
                    current_states = [GPIO.input(pin) for pin in gpio_pins]  
                    print(f"current_states: {current_states}")       

                    # Verificar si hay un cambio en los estados
                    if current_states != last_states:           
                        # Empaquetar el ID del dispositivo y los nuevos estados
                        data = struct.pack('I', device_id) + bytes(current_states)            
                        s.sendall(data)
                        print(f"Datos enviados: {data}")            
                        last_states = current_states

                    # Recibir respuesta del servidor
                    try:
                        response = s.recv(1)  # Espera 1 byte de respuesta
                        if response == b'1':
                            print("Respuesta del servidor: Todo bien")
                        elif response == b'0':
                            print("Respuesta del servidor: Mal, intentando de nuevo")
                            for _ in range(max_retries):
                                # Intentar volver a enviar datos
                                s.sendall(data)
                                response = s.recv(1)
                                if response == b'1':
                                    print("Respuesta del servidor: Todo bien")
                                    break
                    except socket.timeout:
                        print("Tiempo de espera agotado para recibir respuesta del servidor.")

                    time.sleep(1)  # Tiempo entre lecturas (ajustable)

            except Exception as e:
                print(f"Ocurrió un error en la conexión: {e}")

except KeyboardInterrupt:
    print("Interrumpido por el usuario")

finally:
    # Limpiar los GPIO al finalizar
    GPIO.cleanup()
    print("GPIO limpiados")
