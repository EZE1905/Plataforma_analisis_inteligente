import pandas as pd
import uuid

def limpiar_texto(df):
    df["operacion"] = df["operacion"].str.strip().str.lower()
    df["categoria"] = df["categoria"].str.strip().str.lower()
    df["descripcion"] = df["descripcion"].str.strip().str.lower()
    return df

def limpiar_nulos(df):
    df["monto"] = df["monto"].fillna(0)
    df["categoria"] = df["categoria"].fillna("vacio")
    df["descripcion"] = df["descripcion"].fillna("vacio")
    df["operacion"] = df["operacion"].fillna("vacio")
    return df

def limpiar_montos(df):
    df["monto"] = pd.to_numeric(df["monto"], errors="coerce")
    return df

def generar_uuid(df):
    df["id"] = [uuid.uuid4() for _ in range(len(df))]
    return df

def limpiar_dataset(df):
    df = limpiar_texto(df)
    df = limpiar_nulos(df)
    df = limpiar_montos(df)
    df = generar_uuid(df)
    return df