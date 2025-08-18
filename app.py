import os
from pathlib import Path
from functools import lru_cache

import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px


DATA_PATH = Path(__file__).parent / "datos_energia.csv"


def load_data(csv_path=DATA_PATH):
    """Carga el CSV a un DataFrame con índice de fecha en formato datetime.

    - Lee `datos_energia.csv`
    - Convierte la columna `fecha` a datetime
    - Define `fecha` como índice del DataFrame
    - Retorna el DataFrame resultante
    """
    df = pd.read_csv(csv_path)
    df["fecha"] = pd.to_datetime(df["fecha"], errors="raise")
    df = df.set_index("fecha").sort_index()
    return df


@lru_cache(maxsize=1)
def get_cached_data(csv_path=str(DATA_PATH)):
    """Nueva función para cargar datos con caché.

    Envuelve `load_data` y mantiene el resultado en memoria para evitar
    recargas repetidas cuando se reconstruye el layout.
    """
    return load_data(Path(csv_path))


def create_app(dataframe):
    """Crea una app Dash mínima para visualizar la serie temporal."""
    app = Dash(__name__, assets_folder="assets")

    # Elegir columna a graficar: por defecto `consumo_kwh` si existe,
    # de lo contrario la primera columna numérica disponible
    if "consumo_kwh" in dataframe.columns:
        y_col = "consumo_kwh"
    else:
        numeric_cols = dataframe.select_dtypes("number").columns
        y_col = numeric_cols[0] if len(numeric_cols) > 0 else dataframe.columns[0]

    fig = px.line(
        dataframe.reset_index(),
        x="fecha",
        y=y_col,
        title="Producción/Consumo energético",
        labels={"fecha": "Fecha", y_col: "Energía (kWh)"},
    )

    app.layout = html.Div(
        children=[
            html.H1("Tablero de energía"),
            html.P("Serie temporal cargada desde datos_energia.csv"),
            dcc.Graph(id="grafico-energia", figure=fig),
        ]
    )

    return app


if __name__ == "__main__":
    df = get_cached_data()
    app = create_app(df)
    # Escucha en 0.0.0.0 para facilitar despliegue; localmente use http://127.0.0.1:8050
    app.run_server(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 8050)))
