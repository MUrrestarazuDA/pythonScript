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

```




