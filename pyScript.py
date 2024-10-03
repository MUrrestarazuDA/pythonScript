import RPi.GPIO as GPIO
import socket
import time

# Configuración de los GPIOs
GPIO.setmode(GPIO.BCM)  # Numeración BCM
gpio_pins = [17, 27, 22, 23]  # Reemplazar con los pines conectados
# Configuración del socket
HOST = '192.168.1.100'  # Dirección IP del servidor
PORT = 65432            # Puerto del servidor

# Configurar los pines como entradas con resistencias pull-up internas
for pin in gpio_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)



# Crear un socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOST, PORT))
    print(f"Conectado a {HOST}:{PORT}")

    # Almacenar la última lectura de los pines
    last_states = [GPIO.input(pin) for pin in gpio_pins]

    while True:
        # Leer el estado de los GPIOs
        current_states = [GPIO.input(pin) for pin in gpio_pins]        
        if current_states != last_states:           
            data = bytes(current_states)            
            s.sendall(data)
            print(f"Datos enviados: {data}")            
            last_states = current_states

        time.sleep(1) 

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    s.close()
    GPIO.cleanup()
    print("Socket cerrado y GPIO limpiados.")