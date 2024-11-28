import pandas as pd

df = pd.read_csv('./clientes_banco.csv')

df = df.drop_duplicates(subset=['Cliente_ID'])


df.fillna({'Edad': df['Edad'].mean()}, inplace=True)
df.fillna({'Genero': df['Genero'].mode()[0]}, inplace=True)
df.fillna({'Saldo': df['Saldo'].median()}, inplace=True)
df.fillna({'Activo': df['Activo'].mode()[0]}, inplace=True)
df.fillna({'Nivel_de_Satisfaccion': df['Nivel_de_Satisfaccion'].mean()}, inplace=True)

df['Edad'] = df['Edad'].astype(int)
df['Activo'] = df['Activo'].astype(int)
df['Nivel_de_Satisfaccion'] = df['Nivel_de_Satisfaccion'].astype(int)

df.to_csv('./clientes_banco_clean_data.csv', index=False, encoding="utf-8", sep=",")


