# 🔗 Proyecto de Consolidación de Archivos Excel desde OneDrive

Este proyecto tiene como objetivo automatizar la consolidación de múltiples archivos de Excel que están almacenados en OneDrive. Los usuarios tienen acceso a estos archivos a través de enlaces compartidos, donde pueden insertar datos de forma independiente en cada archivo. El objetivo es crear un script en Python que lea estos archivos desde sus respectivas URL, los consolide en un solo archivo y lo actualice periódicamente. Además, se implementará la funcionalidad de subir el archivo consolidado a un repositorio en GitHub.

## 📋 Requerimientos Iniciales

- Leer archivos de Excel desde URL compartidas en OneDrive.
- Consolidar los datos de múltiples archivos en uno solo.
- Actualizar el archivo consolidado periódicamente.
- Subir el archivo consolidado a un repositorio en GitHub.

## 🎯 Planteamiento del Problema

Los usuarios comparten archivos de Excel en OneDrive para que otras personas puedan insertar datos en ellos. Sin embargo, consolidar estos datos manualmente es una tarea tediosa y propensa a errores. Automatizar este proceso facilitará la gestión de los datos y mejorará la eficiencia del flujo de trabajo.

## 🛠️ Posible Solución

La solución propuesta es desarrollar un script en Python que lea los archivos de Excel directamente desde las URL proporcionadas, los consolide en un solo archivo y lo suba a un repositorio en GitHub. Se utilizará la biblioteca `requests` para obtener el contenido de las URL y `openpyxl` para leer los archivos de Excel. El script se ejecutará periódicamente utilizando algún mecanismo de programación de tareas, como cronjobs en sistemas Unix o Programador de tareas en Windows.

## 💻 Tecnologías Utilizadas

- Python
- GitHub
- OneDrive

## 📚 Librerías

- `requests`: Para realizar solicitudes HTTP y obtener el contenido de las URL.
- `openpyxl`: Para leer y escribir archivos de Excel.

## 🔄 Métodos

- Obtener el contenido de los archivos de Excel desde las URL compartidas en OneDrive.
- Consolidar los datos de los archivos en uno solo.
- Convertir el archivo consolidado a formato CSV.
- Subir el archivo consolidado a un repositorio en GitHub.

## 📄 Script

El script principal se encuentra en el archivo `app.py` dentro del directorio `SIMULACRO JMR`.

## 🌐 Servidor

No se requiere un servidor dedicado para este proyecto, ya que se ejecutará localmente en la máquina del usuario. GitHub se utilizará para almacenar y compartir los cambios subidos al repositorio en intervalos regulares de tiempo.

## 🔒 MIT License

Este proyecto se distribuye bajo la Licencia MIT. Consulte el archivo LICENSE para obtener más detalles.

## 🚀 Clonar y Compartir

Puede clonar este repositorio utilizando el siguiente comando:

git clone https://github.com/tu-usuario/nombre-del-repositorio.git


¡No olvides darle una estrellita al repositorio si te ha resultado útil!

