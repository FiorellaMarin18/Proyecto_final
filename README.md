# Proyecto_final

# 📚 Mi Biblioteca

**Mi Biblioteca** es una aplicación web desarrollada con Django que permite a los usuarios llevar un registro personalizado de los libros que han leído o desean leer. Los usuarios pueden agregar, editar, eliminar y ver detalles de sus libros, así como gestionar su estado y reseña personal.

---

## 🚀 Características

- Registro e inicio de sesión personalizados para usuarios.
- CRUD completo de libros (crear, leer, actualizar y eliminar).
- Filtro de libros por usuario autenticado.
- Interfaz con Bootstrap 5 para una apariencia moderna y responsive.

---

## 🛠️ Clonar e instalar el proyecto

1. **Clona el repositorio**
```bash
git clone https://github.com/tu_usuario/mi-biblioteca.git
cd mi-biblioteca


2. **Crea un entorno virtual**
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

3. Instala las dependencias
pip install -r requirements.txt

4. Aplica las migraciones
python manage.py migrate

5. Crea un superusuario (opcional)
python manage.py createsuperuser

▶️ Ejecutar el servidor de desarrollo
python manage.py runserver


📌 Instrucciones adicionales
El panel de administración está disponible en http://127.0.0.1:8000/admin

La base de datos por defecto es MySQl Workbench.

Si agregas nuevas aplicaciones o modelos, no olvides correr makemigrations y migrate.

Asegúrate de tener Django instalado (pip install django) si no estás usando el archivo requirements.txt.

