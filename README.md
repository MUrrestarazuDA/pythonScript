# pythonScript

## Instalación

Actualizacion de bibliotecas disponibles.
```bash
sudo apt-get update
```
Instalacion de python si todavia no lo tiene instalado 

```bash
sudo apt install python3
sudo apt install python3-pip
```


Instalación de la libreria para leer los gpios
```bash
sudo apt-get install python3-rpi.gpio
```

A continuación todos los comandos para ejecutarlos a la vez.

```bash
sudo apt-get update
sudo apt install python3
sudo apt install python3-pip
sudo apt-get install python3-rpi.gpio
```

## Ejecutar script

Dirigirse a la ruta donde esta el script y escribir:

```bash
python3 pyScript.py
```

Esto dejará lanzado el script.

## Configuración para lanzar script al inicio

Para configurar el script al iniciar la raspberry es necesario abir fichero bashhrc.

```bash
sudo nano ~/.bashrc
```
Al final del fichero incluir lo siguiente (asumiendo que el script esta en una ruta del escritorio)

```bash
cd /home/pi/Desktop/pythonRaspberry
while true; do
    python3 pyScript.py >> ~/python_script.log 2>&1
    if [ $? -ne 0 ]; then
        echo "El script falló. Reiniciando..." >> ~/python_script.log
        sleep 5
    else
        break
    fi
done
```

Cerrar el fichero guardando los cambios y reiniciar:

```bash
sudo reboot
```

Para consultar los logs que va generando el script escribir en el terminal:

```bash
tail -f ~/python_script.log
```


## Pines GPIO

![Pines gpio](pines-gpio.jpg)


