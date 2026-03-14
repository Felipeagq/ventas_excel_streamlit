import pandas as pd
import numpy as np

np.random.seed(0)
n = 100

df = pd.DataFrame({
    "Vendedor":   np.random.choice(["Ana", "Luis", "Carlos", "María"], n),
    "Region":     np.random.choice(["Norte", "Sur", "Este", "Oeste"], n),
    "Producto":   np.random.choice(["Laptop", "Mouse", "Teclado", "Monitor"], n),
    "Ventas":     np.random.randint(500, 5000, n),
    "Mes":        np.random.choice(["Enero", "Febrero", "Marzo", "Abril"], n),
})

df.to_excel("ventas.xlsx", index=False)
print("ventas.xlsx creado!")
