# Archivos

- Consorcios - public.png (contiene el diagrama ER)

- DDL.txt contiene definiciones de las tables

- dump-Consorcios-20230501.backup contiene el dump para la creación de la db Consorcios (antes del restore crear la DB (Consorcios)

# Comandos

- Crear models desde base de datos
python manage.py inspectdb > models_importados.txt

- Preparar la migracion desde models
python manage.py makemigrations

- Crear/Modificar tablas en la base de datos
python manage.py migrate