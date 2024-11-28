import pandas as pd

# Import data desde clientes_banco.csv a dataframe de pandas
df = pd.read_csv('./res/clientes_banco.csv')

# Eliminar registros en base a valores repetidos de la columna j
df = df.drop_duplicates(subset=['Cliente_ID'])

df.fillna({'Edad': df['Edad'].mean()}, inplace=True)
df.fillna({'Genero': df['Genero'].mode()[0]}, inplace=True)
df.fillna({'Saldo': df['Saldo'].median()}, inplace=True)
df.fillna({'Activo': df['Activo'].mode()[0]}, inplace=True)
df.fillna({'Nivel_de_Satisfaccion': df['Nivel_de_Satisfaccion'].mean()}, inplace=True)

df['Edad'] = df['Edad'].astype(int)
df['Activo'] = df['Activo'].astype(int)
df['Nivel_de_Satisfaccion'] = df['Nivel_de_Satisfaccion'].astype(int)

df.to_csv('./res/clientes_banco_clean_data.csv', index=False, encoding="utf-8", sep=",")


