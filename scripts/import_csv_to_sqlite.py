'''
Este script importa los datos de csv a la base de datos sqlite3
creada generada por django
'''

import sqlite3
import csv

conn = sqlite3.connect('../pandas-django/db.sqlite3')
cursor = conn.cursor()

with open('../res/clientes_banco_clean_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    cursor.executemany('''
        INSERT INTO restapi_cliente (id_cliente, edad, genero, saldo, estado_actividad, nivel_satisfaccion) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', reader)

conn.commit()
conn.close()
