# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 15:10:12 2025

@author: Camilo Alarcon
"""

import pandas as pd
import glob
import os

# ----------------------------------------------------------
# CONFIGURACIÓN – CAMBIA ESTAS RUTAS SEGÚN TU PROYECTO
# ----------------------------------------------------------
INPUT_DIR = r"C:\Users\Camilo Alarcon\Desktop\Analisis\FinanzasPersonales\data_raw"                 # Carpeta donde están tus Excel
OUTPUT_FILE = "C:/Users/Camilo Alarcon/Desktop/Analisis/FinanzasPersonales/data_clean/tabla_completa.xlsx"
# ----------------------------------------------------------


def unir_archivos(input_dir, output_file):
    # Buscar todos los archivos .xlsx
    archivos = glob.glob(os.path.join(input_dir, "*.xlsx"))

    if len(archivos) == 0:
        raise FileNotFoundError(f"No se encontraron archivos .xlsx en: {input_dir}")

    df_lista = []

    for archivo in archivos:
        df = pd.read_excel(archivo)
        df["archivo_origen"] = os.path.basename(archivo)
        df_lista.append(df)

    tabla_completa = pd.concat(df_lista, ignore_index=True)

    # Crear carpeta de salida si no existe
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Guardar como Excel
    tabla_completa.to_excel(output_file, index=False)

    print(f"Archivo Excel generado en:\n{output_file}")
    print(f"Total de filas: {len(tabla_completa)}")


if __name__ == "__main__":
    unir_archivos(INPUT_DIR, OUTPUT_FILE)
