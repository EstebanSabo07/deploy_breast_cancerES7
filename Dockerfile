# Usa una imagen base con Python
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto donde se ejecuta Streamlit
EXPOSE 8501

# Comando para ejecutar la app
CMD ["streamlit", "run", "main.py"]
