FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
libpq-dev \
nano \
&& rm -rf /var/lib/apt/lists/*

# Copiar los archivos de requerimientos y instalar dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido del proyecto en el contenedor
COPY . .

# Comando para ejecutar el servidor de desarrollo de Django en el puerto 8001
CMD ["python", "tareas/manage.py", "runserver", "0.0.0.0:8000"]

