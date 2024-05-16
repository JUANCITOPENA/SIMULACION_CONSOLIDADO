import pandas as pd
import openpyxl
import requests

def actualizar_consolidado():
    # URLs de los archivos en OneDrive o SharePoint
    urls = [
        "https://onedrive.live.com/edit.aspx?resid=31BA1540EFD54926!18170&cid=31ba1540efd54926&CT=1715875947902&OR=ItemsView",
        "https://onedrive.live.com/edit.aspx?resid=31BA1540EFD54926!18171&cid=31ba1540efd54926&CT=1715875950317&OR=ItemsView",
        "https://onedrive.live.com/edit.aspx?resid=31BA1540EFD54926!18169&cid=31ba1540efd54926&CT=1715875952367&OR=ItemsView",
        "https://onedrive.live.com/edit.aspx?resid=31BA1540EFD54926!18172&cid=31ba1540efd54926&CT=1715875954344&OR=ItemsView",
        "https://onedrive.live.com/edit.aspx?resid=31BA1540EFD54926!18174&cid=31ba1540efd54926&CT=1715875956731&OR=ItemsView",
        "https://onedrive.live.com/edit.aspx?resid=31BA1540EFD54926!18173&cid=31ba1540efd54926&CT=1715875958789&OR=ItemsView",
        "https://onedrive.live.com/edit.aspx?resid=31BA1540EFD54926!18175&cid=31ba1540efd54926&CT=1715875961592&OR=ItemsView",
        "https://onedrive.live.com/edit.aspx?resid=31BA1540EFD54926!18176&cid=31ba1540efd54926&CT=1715875963989&OR=ItemsView",
        "https://onedrive.live.com/edit.aspx?resid=31BA1540EFD54926!18177&cid=31ba1540efd54926&CT=1715875966069&OR=ItemsView",
        "https://onedrive.live.com/edit.aspx?resid=31BA1540EFD54926!18179&cid=31ba1540efd54926&CT=1715875968270&OR=ItemsView"
    ]

    # Leer los datos directamente desde las URL y consolidarlos en un solo DataFrame
    hojas_individuales = []
    for url in urls:
        try:
            # Obtener el contenido del archivo desde la URL
            response = requests.get(url)
            workbook = openpyxl.load_workbook(response.content)
            sheet = workbook.active
            data = sheet.values
            columns = next(data)
            hojas_individuales.append(pd.DataFrame(data, columns=columns))
        except Exception as e:
            print(f"Error al leer el archivo desde la URL: {url}. Error: {str(e)}")

    # Verificar si se encontraron archivos para consolidar
    if not hojas_individuales:
        print("No se encontraron archivos para consolidar.")
        return

    tabla_consolidada = pd.concat(hojas_individuales, ignore_index=True)

    # Convertir la tabla consolidada a formato CSV
    csv_data = tabla_consolidada.to_csv(index=False)

    # Subir el archivo consolidado a GitHub
    # Aquí debes agregar el código para subir el archivo a GitHub

    print("Archivo consolidado creado exitosamente.")

# Llamar a la función para actualizar el consolidado
actualizar_consolidado()
