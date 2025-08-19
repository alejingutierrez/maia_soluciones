# Reporte: Desplegando un tablero en la nube

## Datos del estudiante
- Nombre: Manuel Alejandro Gutiérrez Arango 
- Correo: ma.gutierreza@uniandes.edu.co
- Fecha: 18 de agosto de 2025

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

### Evidencias (salidas de consola)
Git y configuración global:
```bash
$ git --version
git version 2.39.5 (Apple Git-154)

$ git config --global user.name
Alejandro Gutierrez

$ git config --global user.email
malgutierrezar@gmail.com
```

Historial de commits (resumen):
```bash
$ git log --oneline -n 10
05decce Añade gunicorn y detalla pasos de push por HTTPS con PAT en el reporte
b8f9658 Actualiza reporte con URLs del repo, comandos, y guía de ejecución local
92fd5fe Agrega assets y reporte
d3803fe nueva funcion para cargar datos
19f4f69 Implementa load_data() y tablero Dash mínimo; agrega requirements.txt
300afcf mi primer commit
970a501 Primer commit: agrega app.py y datos_energia.csv
```

Remoto configurado:
```bash
$ git remote -v
origin  https://github.com/alejingutierrez/maia_soluciones.git (fetch)
origin  https://github.com/alejingutierrez/maia_soluciones.git (push)
```

Ramas locales y remotas:
```bash
$ git branch -a
  main
* master
  remotes/origin/main
  remotes/origin/master
```

Estado del repositorio:
```bash
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

Archivos presentes:
```bash
$ ls -la
total 32
drwxr-xr-x@  8 agutie04  staff   256 Aug 18 19:20 .
drwxr-xr-x@  3 agutie04  staff    96 Aug 18 19:20 ..
drwxr-xr-x@ 12 agutie04  staff   384 Aug 18 19:23 .git
-rw-r--r--@  1 agutie04  staff  2158 Aug 18 18:51 app.py
drwxr-xr-x@  6 agutie04  staff   192 Aug 18 18:32 assets
-rw-r--r--@  1 agutie04  staff    63 Aug 18 18:30 datos_energia.csv
-rw-r--r--@  1 agutie04  staff  2372 Aug 18 19:21 reporte.md
-rw-r--r--@  1 agutie04  staff    59 Aug 18 19:20 requirements.txt
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

Versión de Python local:
```bash
$ python3 -V
Python 3.9.6
```

### Ejecución en segundo plano (opcional)
Para levantar con gunicorn y dejarlo ejecutando en segundo plano:
```bash
source .venv/bin/activate
nohup gunicorn -w 2 -b 127.0.0.1:8050 app:server > server.log 2>&1 & echo $! > server.pid
```
Detener el servicio:
```bash
kill $(cat server.pid)
```
URL utilizada para la captura del tablero: `http://127.0.0.1:8050`

### Capturas sugeridas
- `git --version`, `git config` (name/email)
- `git log --oneline`
- Repositorio en GitHub mostrando archivos y ramas `main` y `master`
- Tablero ejecutándose en `http://127.0.0.1:8050`

## 6. Push por HTTPS con PAT (según taller)
1) Generar token (PAT): Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token (classic). Scopes: `repo`. Copie el token.
2) Configurar helper de credenciales en macOS:
```bash
git config --global credential.helper osxkeychain
```
3) Hacer push a `master` por HTTPS:
```bash
git push -u origin master
```
En Username use su usuario de GitHub y en Password pegue el token (PAT).
