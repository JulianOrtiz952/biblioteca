# biblioteca

# 📚 Proyecto Django - Biblioteca

Este proyecto es una API REST desarrollada con Django y Django REST Framework. Permite gestionar autores, libros y reseñas de una biblioteca.

---

## 🧰 Tecnologías usadas

- Python 3.10+
- Django
- Django REST Framework

---

## 🚀 Instalación del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/biblioteca.git
cd biblioteca

🚀Crear_Activar_Entorno_Virtual

python -m venv env
# Windows PowerShell:
.\env\Scripts\Activate.ps1
# Linux/macOS:
source env/bin/activate

🚀Instalar_Dependencias
pip install -r requirements.txt

🚀Aplicar_Migraciones
python manage.py makemigrations
python manage.py migrate

🚀Crear_Superusuario (opcional)
python manage.py createsuperuser

🚀Ejecutar_servidor_de_desarrollo
python manage.py runserver

🚀ENDPOINTS

Método	Endpoint	                Descripción
GET 	/autores/	                 Listar todos los autores
POST	/autores/	               Crear un nuevo autor
GET	    /libros/	                   Listar todos los libros
POST	/libros/	                  Crear un nuevo libro
GET	    /resena/	                 Listar todas las reseñas
POST	/resena/	                Crear una nueva reseña
GET	    /libros/detallados	     Listar libros con sus reseñas anidadas

🚀Crear Autor
{
  "nombre": "Gabriel",
  "apellido": "García Márquez",
  "nacionalidad": "Colombiana"
}

🚀Crear Libro
{
  "titulo": "Cien años de soledad",
  "autores": 1,
  "fecha_publicacion": "1967-05-30",
  "resumen": "Una obra emblemática del realismo mágico."
}

🚀Crear Resena
{
  "libro": 1,
  "texto": "Una lectura fascinante.",
  "calificacion": 5
}
```
