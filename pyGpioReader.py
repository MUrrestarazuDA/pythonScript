import RPi.GPIO as GPIO
import time

# Configuración de los GPIOs
GPIO.setmode(GPIO.BCM)  # Numeración BCM
gpio_pins = [26, 5, 6, 13]  # Reemplazar con los pines conectados

# Configurar los pines GPIO
for pin in gpio_pins:
    GPIO.setup(pin, GPIO.IN)  # Configura el pin como entrada

try:
    while True:
        # Leer el estado de los GPIOs
        current_states = [GPIO.input(pin) for pin in gpio_pins]
        
        # Imprimir el estado de los GPIOs
        for pin, state in zip(gpio_pins, current_states):
            print(f"Pin {pin}: {'Alto' if state else 'Bajo'}")

        time.sleep(1)  # Tiempo entre lecturas (ajustable)

except KeyboardInterrupt:
    print("Interrumpido por el usuario")

finally:
    # Limpiar los GPIO al finalizar
    GPIO.cleanup()
    print("GPIO limpiados")
