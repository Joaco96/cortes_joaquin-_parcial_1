from funciones import *

def desplegar_menu():
    print(f"\n-----")
    print(f"MENU PARCIAL 1")
    print(f"-----")
    print(f"1. Cargar archivo CSV")
    print(f"2. Imprimir lista")
    print(f"3. Asignar estadisticas")
    print(f"4. Filtrar por mejores posts")
    print(f"5. Filtrar por haters")
    print(f"6. Informar promedio de followers")
    print(f"7. Ordenar los datos por nombre de user ascendente")
    print(f"8. Mostrar más popular")
    print(f"\n9. Salir del programa")

def main():
        posts=[]
        while True:
            desplegar_menu()
            eleccion = input("\n- Seleccionar una opción: ")
            match eleccion:
                case "1":
                    archivo = input("\n- ingresar nombre del archivo: ")
                    posts = leer_csv(archivo)
                case "2":
                    mostrar_tabla(posts)
                case "3":
                    asignar_stats(posts)
                case "4":
                    extraer_mejores(posts)
                case "5":
                    extraer_peores(posts)
                case "6":
                    promedio_followers(posts)
                case "7":
                    ordenar_datos(posts)
                case "8":
                    mas_popular(posts)
                case "9":
                    return False

main()
