# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)
# README

## Introducción
Este proyecto tiene como finalidad analizar y generar un reporte la data de transacciones de tipo\n
crédito y débito que sea hacen en un periodo determinado.

El Reporte debe contener:
[1] Balance Final: sustracción de los montos de crédito y los de débito
[2] Transaccion de Mayor Monto: identificado por el ID y monto
[3] Conteo de Transacciones: separadas por cada tipo (crédito o débito)

## Instrucciones de Ejecución
[1] Fork en GitHub y clone del repositorio en local:
```
git clone git@github.com:<tu-usuario>/interbank-academy-25.git
```
[2] Cambiar los permisos a ejecucion del archivo exercise.py
[3] Ejecutar el archivo con
```
./exercise.py
```

* Notas adicionales:
    revisar la data entrante del archivo data.csv

## Enfoque y Solución
### Lógica:
[1] cargar el archivo
[2] leer su contenido fila por fila
[3] entender y implementar lo que se pide
[4] generar el reporte

### Diseño:
[1] todo el codebase en un solo archivo
[2] siguiendo una programacion procedimental

## Estructura del Proyecto
### Archivos principales:
[1] README - archivo introductorio donde se plasma la idea y de como lo ponemos a correr
[2] data.csv - data en crudo de las transacciones
[3] exercise.py - codebase donde se analiza e implementa los requerimientos
