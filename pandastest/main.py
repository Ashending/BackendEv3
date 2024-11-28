import pandas as pd

df = pd.read_csv('./clientes_banco_clean_data.csv')

df['Edad'] = df['Edad'].astype(int)
df['Activo'] = df['Activo'].astype(int)
df['Nivel_de_Satisfaccion'] = df['Nivel_de_Satisfaccion'].astype(int)

print(pd.api.types.is_integer_dtype(df['Edad']))
print(pd.api.types.is_integer_dtype(df['Activo']))
print(pd.api.types.is_integer_dtype(df['Nivel_de_Satisfaccion']))

df.to_csv('./clientes_banco_clean_data.csv')
