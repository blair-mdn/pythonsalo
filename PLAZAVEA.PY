import pandas as pd

# ARCHIVO CSV CON LOS DATOS.
df = pd.read_csv('productos.csv')

# 1. PRIMERA ACTIVIDAD
print("1. Mostrar los 10 primeros productos:")
print(df.head(10))
print("\n")

# 2. SEGUNDA ACTIVIDAD
menor_precio_lista = df.loc[df['Precio Lista'].idxmin()]
print("2. El producto con menor precio lista es:")
print(menor_precio_lista)
print("\n")

# 3. TERCERA ACTIVIDAD
mayor_precio_oh = df.loc[df['Precio Oh'].idxmax()]
print("3. El producto con mayor precio Oh es:")
print(mayor_precio_oh)
print("\n")

# 4. CUARTA ACTIVIDAD
precio_online_promedio = df['Precio Online'].mean()
print(f"4. El precio online promedio de todos los productos es: {precio_online_promedio:.2f}")
print("\n")


