# TO-DO App con Flask, Docker y PostgreSQL

[![CI/CD Pipeline](https://github.com/tu-usuario/TO-DO-app/actions/workflows/main.yml/badge.svg)](https://github.com/tu-usuario/TO-DO-app/actions)
[![Docker Image](https://img.shields.io/badge/Docker-Available-blue)](https://hub.docker.com/r/tu-usuario/todo-app)

Aplicación de lista de tareas con integración DevOps completa. Perfecta para aprender Docker, CI/CD y despliegues cloud.

## 🚀 Características
- ✅ CRUD de tareas con Flask
- 🐳 Docker Compose para PostgreSQL y LocalStack (S3 local)
- 📦 CI/CD con GitHub Actions
- 📤 Subida de archivos a AWS S3 (emulado con LocalStack)
- 🔄 Despliegue automático en Render/Heroku

## 🛠️ Tecnologías
| **Categoría**       | **Herramientas**                          |
|----------------------|-------------------------------------------|
| Backend              | Flask, SQLAlchemy                         |
| Base de Datos        | PostgreSQL                                |
| DevOps               | Docker, GitHub Actions                    |
| Almacenamiento       | AWS S3 (LocalStack para desarrollo local) |
| Pruebas              | Pytest                                    |

## 🖥️ Instalación Local
```bash
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/TO-DO-app.git
cd TO-DO-app

# 2. Iniciar servicios (Flask + PostgreSQL + LocalStack)
docker-compose up --build

# 3. Acceder a la aplicación
http://localhost:5000