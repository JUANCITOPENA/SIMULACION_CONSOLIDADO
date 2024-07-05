# Debes Instalar en la Consola cada una de Estas Librerias.
# pip install pandas numpy

# Importar las Librerias:

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Datos originales para replicar en cada archivo (puedes agregar la URL local de los Archivos que quieras)
data = [
    ["1/3/2023", "Gorro (M, Gris, Patagonia)", 5, 20, "$100.00", "Accesorios", "Norte"],
    ["2/10/2023", "Sudadera (L, Roja, Under Armour)", 3, 40, "$120.00", "Ropa", "Sur"],
    ["3/15/2023", "Reloj (Único, Plata, Casio)", 2, 60, "$120.00", "Accesorios", "Este"],
    ["4/22/2023", "Mochila (M, Negra, North Face)", 4, 80, "$320.00", "Accesorios", "Norte"],
    ["5/30/2023", "Gorra (Único, Azul, Nike)", 7, 15, "$105.00", "Accesorios", "Sur"],
    ["6/5/2023", "Chaqueta (M, Negra, Columbia)", 2, 100, "$200.00", "Ropa", "Norte"],
    ["7/11/2023", "Calcetines (L, Blanco, Puma)", 10, 5, "$50.00", "Accesorios", "Este"],
    ["8/18/2023", "Bufanda (Única, Roja, Gucci)", 1, 150, "$150.00", "Accesorios", "Sur"],
    ["9/22/2023", "Botas (43, Marrón, Dr. Martens)", 3, 120, "$360.00", "Calzado", "Norte"],
    ["10/5/2023", "Traje (M, Azul, Armani)", 1, 300, "$300.00", "Ropa", "Este"],
    ["11/19/2023", "Vestido (L, Verde, Zara)", 2, 45, "$90.00", "Ropa", "Sur"],
    ["12/12/2023", "Sandalias (38, Negro, Birkenstock)", 6, 35, "$210.00", "Calzado", "Norte"],
    ["1/5/2024", "Gafas de Sol (Único, Negro, Ray-Ban)", 3, 120, "$360.00", "Accesorios", "Este"],
    ["2/9/2024", "Guantes (M, Negro, Reebok)", 8, 25, "$200.00", "Accesorios", "Sur"],
    ["3/21/2024", "Corbata (Única, Roja, Hugo Boss)", 5, 30, "$150.00", "Accesorios", "Norte"],
    ["4/27/2024", "Falda (S, Negra, H&M)", 4, 35, "$140.00", "Ropa", "Este"],
    ["5/13/2024", "Chaqueta (L, Verde, Patagonia)", 2, 150, "$300.00", "Ropa", "Norte"],
    ["6/10/2024", "Maleta (M, Azul, Samsonite)", 3, 100, "$300.00", "Accesorios", "Sur"],
    ["7/25/2024", "Zapatos de Deporte (40, Blanco, New Balance)", 5, 70, "$350.00", "Calzado", "Este"],
    ["5/13/2024", "Paraguas (Único, Negro, Totes)", 6, 25, "$150.00", "Accesorios", "Norte"],
    ["6/10/2024", "Zapatos (41, Negro, Nike)", 1, 50, "$50.00", "Calzado", "Norte"],
    ["7/25/2024", "Camiseta (S, Negra, Adidas)", 1, 15, "$15.00", "Ropa", "Este"],
    ["5/13/2024", "Camiseta (M, Azul, Nike)", 4, 15, "$60.00", "Ropa", "Norte"],
    ["6/10/2024", "Pantalón (L, Gris, Levi's)", 6, 25, "$150.00", "Ropa", "Este"],
    ["7/25/2024", "Zapatos (42, Negro, Nike)", 9, 50, "$450.00", "Calzado", "Norte"]
]

# Función para generar fechas aleatorias dentro de un rango
def generate_random_dates(start_date, end_date, num_dates):
    start_date = datetime.strptime(start_date, "%Y/%m/%d")
    end_date = datetime.strptime(end_date, "%Y/%m/%d")
    date_range = end_date - start_date
    random_dates = [start_date + timedelta(days=random.randint(0, date_range.days)) for _ in range(num_dates)]
    return random_dates

# Función para crear archivos Excel con datos aleatorios
def create_excel_files(num_files, start_date, end_date):
    for i in range(num_files):
        # Generar datos aleatorios de fechas y cantidades
        random_dates = generate_random_dates(start_date, end_date, len(data))
        random_quantities = np.random.randint(1, 11, size=len(data))  # Cantidades aleatorias entre 1 y 10
        
        # Copiar datos originales y actualizar fechas y cantidades
        new_data = []
        for idx, row in enumerate(data):
            new_row = row[:]
            new_row[0] = random_dates[idx].strftime("%m/%d/%Y")  # Actualizar fecha
            new_row[2] = random_quantities[idx]  # Actualizar cantidad
            new_data.append(new_row)
        
        # Crear DataFrame y guardar en archivo Excel
        df = pd.DataFrame(new_data, columns=["Fecha", "Nombre del Producto", "Cantidad Vendida", "Precio Unitario",
                                             "Total de Venta", "Categoría", "Región"])
        filename = f"ventas_USUARIO{i + 71}.xlsx"  # ventas_USUARIO1.xlsx, ventas_USUARIO2.xlsx, ...
        df.to_excel(filename, index=False)
        print(f"Archivo '{filename}' creado exitosamente.")

# Ejemplo de uso
num_archivos = 80
fecha_inicio = "2001/01/20"
fecha_fin = "2024/7/5"
create_excel_files(num_archivos, fecha_inicio, fecha_fin)
