# utf-8 encoding for spanish characters 

# %% 
# librerias 
import yaml
# %%
# creacion de archivo yml
def creacion_archivo(nombre_archivo, data):
    '''
    Crea un archivo YAML con los datos proporcionados.
    args: 
        nombre_archivo (str) - Nombre del archivo YAML a crear.
        data (dict) - Datos a escribir en el archivo YAML.
    '''
    # Escribir en el archivo YAML
    with open(nombre_archivo, 'w') as file:
        yaml.dump(data, file)

def abrir_archivo(nombre_archivo):
    '''
    Abre un archivo YAML y devuelve su contenido.
    args: 
        nombre_archivo (str) - Nombre del archivo YAML a abrir.
    returns: 
        data (dict) - Contenido del archivo YAML.
    '''
    # Cargar el archivo YAML
    with open(nombre_archivo, 'r') as file:
        data = yaml.safe_load(file)
    return data


def elimina_archivo(nombre_archivo,key_objetivo,valor_eliminar):
    '''
    elimina un valor_eliminar del archivo yml
    args: 
        nombre_archivo (str) - Nombre del archivo YAML a editar.
        key_objetivo (str) - Nombre de la clave que contiene el valor_eliminar a eliminar del archivo YAML.
        valor_eliminar (str) - Nombre del valor_eliminar a eliminar del archivo YAML.
    '''
    data = abrir_archivo(nombre_archivo)
    # Eliminar el valor "azul"
    if valor_eliminar in data[key_objetivo]:
        data[key_objetivo].remove(valor_eliminar)

    # Sobrescribir el archivo YAML
    with open(nombre_archivo, 'w') as file:
        yaml.dump(data, file)
