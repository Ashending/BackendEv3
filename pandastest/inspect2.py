import pandas as pd

df = pd.read_csv('./clientes_banco.csv')

filter_duplicates_by_id = df.drop_duplicates(['Cliente_ID'])
print(filter_duplicates_by_id.describe())


id_cliente = filter_duplicates_by_id['Cliente_ID']
edad = filter_duplicates_by_id['Edad']
genero = filter_duplicates_by_id['Genero']
saldo = filter_duplicates_by_id['Saldo']
activo = filter_duplicates_by_id['Activo']
nivel_satisfaccion = filter_duplicates_by_id['Nivel_de_Satisfaccion']

# print(f"id null: {id_cliente.isnull().sum()}")
# print(f"id repeated: {id_cliente.duplicated().sum()}")
# print(f"edad null: {edad.isnull().sum()}")
# print(f"genero null: {genero.isnull().sum()}")
# print(f"saldo null: {saldo.isnull().sum()}")
# print(f"activo null: {activo.isnull().sum()}")
# print(f"nivel_satisfaccion null: {nivel_satisfaccion.isnull().sum()}")

print(f"mean edad: {edad.mean()} std: {edad.std()}")
print(f"mean saldo: {saldo.mean()} std: {saldo.std()}")
print(f"mean activo: {activo.mean()} std: {activo.std()}")
print(f"mean nivel_satisfaccion: {nivel_satisfaccion.mean()} std: {nivel_satisfaccion.std()}")

