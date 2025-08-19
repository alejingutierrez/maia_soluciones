import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

def load_data(path="datos_energia.csv"):
    """
    Carga los datos de energía desde un archivo CSV.
    
    Args:
        path (str): Ruta al archivo CSV
        
    Returns:
        pd.DataFrame: DataFrame con los datos de energía procesados
    """
    try:
        # Cargar el CSV
        df = pd.read_csv(path)
        
        # Detectar automáticamente la columna de fecha
        posibles_fechas = [c for c in df.columns if c.lower() in ("fecha", "date", "fecha_hora", "datetime", "tiempo")]
        
        if posibles_fechas:
            col_fecha = posibles_fechas[0]
            # Convertir a datetime con manejo de errores
            df[col_fecha] = pd.to_datetime(df[col_fecha], errors="coerce", dayfirst=True)
            # Usar como índice y ordenar
            df = df.set_index(col_fecha).sort_index()
        else:
            # Fallback: usar la primera columna como fecha
            df = pd.read_csv(path, parse_dates=[0], index_col=0).sort_index()
        
        # Remover timezone si existe
        if df.index.tz is not None:
            df.index = df.index.tz_convert(None)
            
        return df
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return pd.DataFrame()

# Cargar datos
df = load_data()

# Layout de la aplicación
app.layout = html.Div([
    html.H1("⚡ Dashboard de Energía - Análisis en Tiempo Real", style={'textAlign': 'center', 'color': '#2c3e50', 'fontSize': '2.5em', 'marginBottom': '20px'}),
    
    html.Div([
        html.H3("Datos de Consumo Energético", style={'color': '#34495e'}),
        html.P(f"Total de registros: {len(df)}", style={'color': '#7f8c8d'}),
        html.P(f"Período: {df.index.min().strftime('%Y-%m-%d')} a {df.index.max().strftime('%Y-%m-%d')}", 
               style={'color': '#7f8c8d'})
    ], style={'margin': '20px', 'padding': '20px', 'backgroundColor': '#ecf0f1', 'borderRadius': '10px'}),
    
    html.Div([
        dcc.Graph(
            id='energia-graph',
            figure=px.line(df, title="Consumo de Energía a lo largo del tiempo")
            if not df.empty else go.Figure().add_annotation(text="No hay datos disponibles", xref="paper", yref="paper")
        )
    ], style={'margin': '20px'}),
    
    html.Div([
        html.H4("Estadísticas", style={'color': '#2c3e50'}),
        html.Div(id='stats-content')
    ], style={'margin': '20px', 'padding': '20px', 'backgroundColor': '#ecf0f1', 'borderRadius': '10px'})
])

@app.callback(
    Output('stats-content', 'children'),
    Input('energia-graph', 'figure')
)
def update_stats(figure):
    if df.empty:
        return html.P("No hay datos para mostrar estadísticas")
    
    # Calcular estadísticas básicas
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    if len(numeric_cols) > 0:
        stats = []
        for col in numeric_cols[:3]:  # Mostrar solo las primeras 3 columnas numéricas
            stats.append(html.Div([
                html.Strong(f"{col}: "),
                html.Span(f"Min: {df[col].min():.2f}, Max: {df[col].max():.2f}, Prom: {df[col].mean():.2f}")
            ], style={'margin': '5px 0'}))
        return stats
    else:
        return html.P("No se encontraron columnas numéricas para análisis")

if __name__ == '__main__':
    print("🚀 Iniciando Dashboard de Energía...")
    print("📊 Abre tu navegador en: http://127.0.0.1:8050")
    print("⏹️  Para detener: CTRL+C")
    app.run_server(debug=True, host='127.0.0.1', port=8050)
