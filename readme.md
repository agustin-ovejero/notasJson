# Instruciones para levantar el proyecto 
1. Instalar python en el sistema
2. crear un entorn virtual
- **En windows** `python -m venv nombre_del_entorno`
- **En Linux** `python3 -m venv nombre_del_entorno`
3. Activar el entorno virtual
- **En Windows** `python source nombre_del_entorno/bin/activate`
- **En Linux** `python3 source nombre_del_entorno/bin/activate`
3. Instalar las dependecias
- pip install -r requirements.txt
4. Levantar el proyecto
- **Nota: Dentro de nada va a cambiar la forma de levantar el proyecto**
- **En Windows** `python main.py`
- **En linux** `python3 main.py`
# Migraciones con Flask-Migrate
## Gestión de Base de Datos

Este proyecto utiliza **Flask-Migrate** para manejar los cambios en los modelos. 
Cada vez que realices un cambio en la estructura (modelos), seguí estos pasos:

1. **Generar la migración:** (Detecta los cambios y crea el script)
   ```bash
   flask db migrate -m "Descripción del cambio"
2. **Aplicar los cambios:** Impacta los cambios en la base de datos
   ```bash
   flask db upgrade

**Para volver a la versión anterior de la base de datos por algun error, ejecuta el siguente comando.**
   ```bash
   flask db downgrade
