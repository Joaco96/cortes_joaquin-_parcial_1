import random
import json
from utils import *

def leer_csv(archivo: str) -> list:
    """_summary_

    Args:
        archivo (str): recibe el archivo format csv.

    Returns:
        list: devuelve una lista con la lectura del archivo.
    """
    posts = []
    import os
    try:
        with open(os.path.join(os.path.dirname(__file__),archivo), "r", encoding="utf-8") as csv:
            encabezado = csv.readline().strip("\n").split(",")
            for linea in csv:
                persona = {}
                linea = linea.strip("\n").split(",")
                id, user, likes, dislikes, followers = linea
                persona["id"] = int(id)
                persona["user"] = user
                persona["likes"] = likes
                persona["dislikes"] = dislikes
                persona["followers"] = int(followers)
                posts.append(persona)
        print("\n-----------------------------")
        print("\n¡Se cargo el archivo con exito!\n")
        print("-----------------------------")
        return posts
    except:
        print("\n-----------------------------")
        print("\nNombre de archvo invalido, pruebe nuevamente\n")
        print("-----------------------------")

def imprimir_user(user:dict) -> None:
    """_summary_

    Args:
        user (dict): recibe la lista con usuarios para imprimirlos linea por linea.
    """
    print(f'{user["id"]:<3} {user["user"]:20} {user["likes"]:<10} {user["dislikes"]:<10} {user["followers"]:<10}')

def mostrar_tabla(posts:list) -> None:
    """_summary_

    Args:
        posts (list): recibe la lista de posts y devuelve la tabla por consola.
    """
    print("\nId  User                 Likes      Dislikes   Followers")
    print("-------------------------------------------------------")
    if(posts):
        for i in range(len(posts)):
            imprimir_user(posts[i])
    else:
        print("\n-----------------------------")
        print("\nTodavia no se cargo el archivo\n")
        print("-----------------------------")

def generar_aleatorio(desde:int,hasta:int) -> int:
    """_summary_

    Args:
        desde (int): recibe el valor inicial del valor aleatorio.
        hasta (int): recibe el valor final del valor aleatorio.

    Returns:
        int: devuelve el valor aleatorio en el rango recibido.
    """
    valor = random.randint(desde,hasta)
    return valor

def asignar_stats(posts:list) -> None:
    """_summary_

    Args:
        posts (list): recibe los posts a los cuales les asigna valores aleatorios de likes, dislikes y followers con sus rangos.
    """
    for user in posts:
        user["likes"] = generar_aleatorio(500,3000)
        user["dislikes"] = generar_aleatorio(300,3500)
        user["followers"] = generar_aleatorio(10000,20000)
    print("\n-----------------------------")
    print("\n¡Asignacion exitosa!\n")
    print("-----------------------------")

def extraer_mejores(posts:list) -> None:
    """_summary_

    Args:
        posts (list): recibe los posts para filtrar los que tienen mas likes y exportar a csv.
    """
    nueva_lista = filter(lambda user: user["likes"] > 2000, posts)
    generar_nuevo_csv(nueva_lista,"mejores_posts.csv")

def generar_nuevo_csv(posts:list,nombre:str) -> None:
    """_summary_

    Args:
        posts (list): recibe la lista de posts para exportar a formato csv.
        nombre (str): recibe el nombre del nuevo archivo csv.
    """
    import os
    with open(os.path.join(os.path.dirname(__file__),nombre), "w", encoding="utf-8") as csv:
        separacion = ","
        csv.write(f"{separacion.join(list(posts[0].keys()))}\n")
        for user in posts:
            valores_user = list(user.values())
            for i in range(len(valores_user)):
                if isinstance(valores_user[i], int) or isinstance(valores_user[i], float) or isinstance(valores_user[i],str):
                    valores_user[i] = str(valores_user[i])
            csv.write(f"{separacion.join(valores_user)}\n")

def extraer_peores(posts:list) -> None:
    """_summary_

    Args:
        posts (list): recibe los posts para filtrar los que tienen mas dislikes que likes y exportar a csv.
    """
    nueva_lista = filter(lambda user: user["dislikes"] > user["likes"], posts)
    generar_nuevo_csv(nueva_lista,"peores_posts.csv")

def promedio_followers(posts:list) -> None:
    """_summary_

    Args:
        posts (list): recibe los posts para calcular el promedio de followers de todos los uauarios y mostrarlo por consola.
    """
    followers_list = map(lambda user: float(user["followers"]), posts)
    sumatoria =  custom_reduce(lambda ant, act: ant + act, followers_list)
    promedio = sumatoria / len(followers_list)
    print(followers_list)
    print(sumatoria)
    print("\n-----------------------------")
    print(f"El promedio de followers es: {round(promedio,2)}")
    print("-----------------------------")

def ordenar_datos(posts:list) -> None:
    """_summary_

    Args:
        posts (list): recibe los posts para ordenarlos de manera ascendente y exportar a json.
    """
    sort(lambda a,b: a["user"] > b["user"] ,posts)
    generar_nuevo_json(posts,"posts_ordenados.json")

def generar_nuevo_json(posts:list,nombre:str) -> None:
    """_summary_

    Args:
        posts (list): recibe la lista de posts para exportar a formato json.
        nombre (str): recibe el nombre del nuevo archivo json.
    """
    import os
    with open(os.path.join(os.path.dirname(__file__),nombre), "w", encoding="utf-8") as archivo:
        json.dump(posts,archivo,indent=4)

def mas_popular(posts:list) -> None:
    """_summary_

    Args:
        posts (list): recibe la lista de posts para mostrar por consola el post con mas likes y su usuario.
    """
    popular = custom_reduce(lambda ant, act: ant if ant["likes"] > act["likes"] else act ,posts)
    print("\n-----------------------------")
    print(f"El nombre del usuario con el posteo mas likeado es: {popular["user"]} con {popular["likes"]} likes ")
    print("-----------------------------")