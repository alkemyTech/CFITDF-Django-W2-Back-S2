<<<<<<< Updated upstream
# Instrucciones para levantar el proyecto Django

## 1. Clonar el repositorio

```bash
git clone https://github.com/alkemyTech/CFITDF-Django-W2-Back-S2.git
cd CFITDF-Django-W2-Back-S2
```

## 2. Crear y activar un entorno virtual

**En sistemas Unix/macOS:**

```bash
python -m venv env
source env/bin/activate
```

**En Windows:**

```bash
python -m venv env
env\Scripts\activate
```

## 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## 4. Aplicar las migraciones

```bash
python manage.py migrate
```

## 5. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor se iniciará normalmente en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)