import os

# Ruta de la carpeta con las fotos
folder_path = r'C:\Users\noahs\OneDrive\Desktop\wetransfer_img_0063-jpeg_2024-09-09_2133'

# Obtener una lista de todos los archivos en la carpeta
files = sorted(os.listdir(folder_path))

# Filtrar solo los archivos .jpg o .jpeg
jpg_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg'))]

# Contadores para el esquema de nombres
book_start = 123  # Libro inicial
book_index = 0    # Contador para el número de libro
file_index = 0    # Contador para a, b, c

# Iterar sobre los archivos y renombrarlos
for file in jpg_files:
    if file_index == 3:  # Si hemos asignado 3 archivos a un libro, incrementamos el número del libro
        file_index = 0
        book_index += 1
    
    # Crear el nuevo nombre del archivo
    suffix = chr(97 + file_index)  # Convertir el índice en una letra (a, b, c, etc.)
    new_name = f"{book_start + book_index}{suffix}.jpg"
    
    # Crear las rutas completas
    old_file = os.path.join(folder_path, file)
    new_file = os.path.join(folder_path, new_name)
    
    # Renombrar el archivo
    os.rename(old_file, new_file)
    
    # Incrementar el contador de archivos
    file_index += 1

print("Renombrado completado.")

