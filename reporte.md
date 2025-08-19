# Reporte: Desplegando un tablero en la nube

## Datos del estudiante
- Nombre:
- Correo:
- Fecha:

## 1. Configuración de Git y repositorio
- Versión de Git: (captura de pantalla)
- Configuración user.name y user.email: (captura)
- Inicialización del repositorio: (captura)

### Repositorio remoto
- URL (HTTPS): `https://github.com/alejingutierrez/maia_soluciones`
- URL (SSH): `git@github.com:alejingutierrez/maia_soluciones.git`

### Comandos ejecutados principales
```bash
git init
git config --global user.name "<tu-usuario>"
git config --global user.email "<tu-email>"
git add app.py datos_energia.csv
git commit -m "Primer commit: agrega app.py y datos_energia.csv"
git add assets/base.css assets/clinical-analytics.css
git commit -m "mi primer commit"
git remote add origin https://github.com/alejingutierrez/maia_soluciones.git
git branch -M main
git push -u origin main
git checkout -b master
git add app.py
git commit -m "nueva funcion para cargar datos"
git add assets reporte.md
git commit -m "Agrega assets y reporte"
git push -u origin master
```

## 2. Estructura del proyecto
- Archivos agregados: `app.py`, `datos_energia.csv`, carpeta `assets/`
- Breve explicación de cada archivo.

## 3. Primer commit
- Comandos utilizados: `git add`, `git commit`
- Mensaje del commit:
- Captura de `git log --oneline`.

## 4. Despliegue en la nube
Este taller se completó hasta antes del despliegue en la nube.

## 5. Ejecución local del tablero
### Requisitos
- Python 3.9

### Instalación
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Ejecución
```bash
python app.py
```
- Abrir en el navegador: `http://127.0.0.1:8050`

### Capturas sugeridas
- `git --version`, `git config` (name/email)
- `git log --oneline`
- Repositorio en GitHub mostrando archivos y ramas `main` y `master`
- Tablero ejecutándose en `http://127.0.0.1:8050`
