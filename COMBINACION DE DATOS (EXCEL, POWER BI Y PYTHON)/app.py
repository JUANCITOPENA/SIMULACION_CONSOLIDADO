# En la consola Instalar estas librerias:

# pip install pandas PyGithub schedule certifi

# Importar cada libreria:
import os
import pandas as pd
from github import Github
import schedule
import time
import datetime
import certifi

# Establecer la variable de entorno REQUESTS_CA_BUNDLE para Python
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# Establecer la variable de entorno REQUESTS_CA_BUNDLE para la línea de comandos (Windows)
os.system('setx REQUESTS_CA_BUNDLE "C:\\Program Files\\PostgreSQL\\16\\ssl\\certs\\ca-bundle.crt"')

def actualizar_consolidado():
    print("Ejecutando actualización a las:", datetime.datetime.now())
    # Leer datos de las hojas individuales y consolidarlos en una sola tabla
    hojas_individuales = []
    for i in range(1, 85):  # Cambia el rango según la cantidad de archivos que tengas
        nombre_archivo = f'ventas_USUARIO{i}.xlsx' # Este es el archivo que se combinara, se leera cada uno de los Archivos.
        if os.path.exists(nombre_archivo):
            df = pd.read_excel(nombre_archivo, engine='openpyxl')
            hojas_individuales.append(df)
            
    # Verificar si se encontraron archivos para consolidar
    if not hojas_individuales:
        print("No se encontraron archivos para consolidar.")
        return
    
    tabla_consolidada = pd.concat(hojas_individuales, ignore_index=True)
    
    # Convertir la columna de fecha al formato adecuado (si es necesario)
    if 'fecha' in tabla_consolidada:
        tabla_consolidada['fecha'] = pd.to_datetime(tabla_consolidada['fecha'], errors='coerce')
    
    # Escribir la tabla consolidada en un archivo Excel
    ruta_archivo_excel = 'consolidado.xlsx'
    tabla_consolidada.to_excel(ruta_archivo_excel, index=False)
    
    # Escribir la tabla consolidada en un archivo CSV
    ruta_archivo_csv = 'consolidado.csv'
    tabla_consolidada.to_csv(ruta_archivo_csv, index=False)
    
    # Escribir la tabla consolidada en un archivo JSON
    ruta_archivo_json = 'consolidado.json'
    tabla_consolidada.to_json(ruta_archivo_json, orient='records', date_format='iso')
    
    # Subir los archivos consolidados a GitHub
    github = Github("TU TOKEN AQUI DE GITHUB")
    repo_nombre = 'SIMULACION_CONSOLIDADO'
    repo = github.get_user().get_repo(repo_nombre)
    
    # Subir el archivo Excel
    with open(ruta_archivo_excel, 'rb') as archivo_excel:
        contenido_excel = archivo_excel.read()
        try:
            # Intentar crear el archivo
            repo.create_file(ruta_archivo_excel, "Actualización automática (Excel)", contenido_excel)
        except Exception as e:
            # Si ya existe, obtener el sha del archivo y actualizarlo
            sha = repo.get_contents(ruta_archivo_excel).sha
            repo.update_file(ruta_archivo_excel, "Actualización automática (Excel)", contenido_excel, sha)
    
    # Subir el archivo CSV
    with open(ruta_archivo_csv, 'rb') as archivo_csv:
        contenido_csv = archivo_csv.read()
        try:
            # Intentar crear el archivo
            repo.create_file(ruta_archivo_csv, "Actualización automática (CSV)", contenido_csv)
        except Exception as e:
            # Si ya existe, obtener el sha del archivo y actualizarlo
            sha = repo.get_contents(ruta_archivo_csv).sha
            repo.update_file(ruta_archivo_csv, "Actualización automática (CSV)", contenido_csv, sha)
    
    # Subir el archivo JSON
    with open(ruta_archivo_json, 'rb') as archivo_json:
        contenido_json = archivo_json.read()
        try:
            # Intentar crear el archivo
            repo.create_file(ruta_archivo_json, "Actualización automática (JSON)", contenido_json)
        except Exception as e:
            # Si ya existe, obtener el sha del archivo y actualizarlo
            sha = repo.get_contents(ruta_archivo_json).sha
            repo.update_file(ruta_archivo_json, "Actualización automática (JSON)", contenido_json, sha)

# Programar la ejecución del script cada 10 segundos
schedule.every(10).seconds.do(actualizar_consolidado)

while True:
    schedule.run_pending()
    time.sleep(1)
