# Dashboard de Energía

Este proyecto implementa un dashboard interactivo para visualizar datos de consumo energético utilizando Dash y Plotly.

## Características

- 📊 Visualización de datos de consumo energético
- 📈 Gráficos interactivos con Plotly
- 🎨 Interfaz moderna y responsive
- 📱 Compatible con dispositivos móviles

## Instalación

1. Clona el repositorio:
```bash
git clone git@github.com:alejingutierrez/maia_soluciones.git
cd maia_soluciones
```

2. Crea un entorno virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install dash pandas plotly numpy
```

## Uso

Ejecuta la aplicación:
```bash
python app.py
```

Abre tu navegador en: http://127.0.0.1:8050

## Estructura del Proyecto

```
├── app.py              # Aplicación principal Dash
├── datos_energia.csv   # Datos de ejemplo
├── assets/             # Archivos estáticos (CSS, JS)
│   └── style.css      # Estilos personalizados
└── README.md          # Este archivo
```

## Funcionalidades

- **load_data()**: Función robusta para cargar datos CSV con detección automática de columnas de fecha
- **Dashboard interactivo**: Gráficos de línea con estadísticas en tiempo real
- **Manejo de errores**: Gestión robusta de archivos faltantes y datos corruptos

## Tecnologías

- **Dash**: Framework web para aplicaciones analíticas
- **Plotly**: Biblioteca de visualización interactiva
- **Pandas**: Manipulación y análisis de datos
- **Python 3.12+**: Lenguaje de programación

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
