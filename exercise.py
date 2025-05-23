#!/usr/bin/env python3

"""
exercise.py

This module offers a funct to read, parse and process a csv file.
It's intended to be used as a data processing tool.

Function:
    - create_report(file): formulates a bank report

Author: Andre Farfan
"""

import csv # importamos el modulo CSV para la correcta lectura

def create_report(file):
    """function that analizes and prints a bank report

    Args:
        file(str): raw data

    Returns:
        none
    """

    try:
        with open(file, newline='', encoding='utf-8') as csvfile:
            number_credit = 0 # iniciamos las variables globales
            number_debit = 0
            sum_credit = 0
            sum_debit = 0
            max_value = 0
            id_max = None
            lector = csv.reader(csvfile) # creamos un objeto reader del modulo

            next(lector)

            for fila in lector:
                id_actual = fila[0]

                try:
                    monto_actual = float(fila[2])
                except ValueError:
                    print(f"Error: el monto {fila[2]} en la transaccion {id_actual} no es valido. Registro ignorado")
                    continue

                if monto_actual > max_value: # if que determina el max_value por cada iteracion
                    max_value = monto_actual
                    id_max = id_actual

                if fila[1] == "Débito": # if que cuenta el numero de operaciones y monto de cada tipo
                    number_debit += 1
                    sum_debit += float(fila[2])
                elif fila[1] == "Crédito":
                    number_credit += 1
                    sum_credit += float(fila[2])

            # Generacion del reporte con lo requerido
            print("Reporte de Transacciones\n-------------------------------------")
            print(f"Balance Final: {round(sum_credit - sum_debit, 2)}")
            print(f"Transacción de Mayor Monto: ID {id_max} - {max_value}")
            print(f"Conteo de Transacciones: Crédito: {number_credit} Débito: {number_debit}")

    except FileNotFoundError:
        print("Archivo no encontrado")
       

if __name__ == '__main__':
    create_report('data.csv')
