# Dockerfile
# Gunakan image Python resmi sebagai base image
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Copy file requirements.txt ke working directory
COPY requirements.txt .

# Install dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh proyek ke working directory
COPY . .

# Expose port yang akan digunakan (jika diperlukan)
EXPOSE 8080

# Command untuk menjalankan aplikasi
CMD ["python", "mental_health_app/main.py"]
