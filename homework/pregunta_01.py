import pandas as pd
import os
"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    if os.path.exists('files/output/solicitudes_de_credito.csv'):
        os.remove('files/output/solicitudes_de_credito.csv')
    
    ruta = 'files/input/solicitudes_de_credito.csv'
    df = pd.read_csv(ruta, sep=';', index_col=0, encoding='UTF-8')

    columnas = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "monto_del_credito", "línea_credito"]

    for colum in columnas:
        if colum in df.columns:
            df[colum] = df[colum].str.lower().str.strip().str.replace("_", " ").str.replace("-", " ").str.replace(",", "").str.replace("$", "").str.replace(".00", "").str.strip()

    df['idea_negocio'] = df['idea_negocio'].str.replace(' ','_').str.replace('-','_').str.strip('_')
    df['estrato'] = df['estrato'].astype(int)
    df['barrio'] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    df['monto_del_credito'] = pd.to_numeric(df["monto_del_credito"], errors="coerce")
    df['comuna_ciudadano'] = pd.to_numeric(df["comuna_ciudadano"], errors="coerce", downcast="integer")
    df['fecha_de_beneficio'] = df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce").combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))

    df = df.drop_duplicates()
    df = df.dropna()

    df.to_csv('files/output/solicitudes_de_credito.csv', sep=';', index=False)

pregunta_01()
