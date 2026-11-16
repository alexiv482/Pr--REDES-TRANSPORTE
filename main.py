from codigo_fuente import *


def seleccionar_red():
    print("\n=== GESTOR DE RUTAS DE TRANSPORTE (FASE 1) ===")
    print("1. Red propia (12 estaciones: D1 - D12)")
    print("2. Red de prueba estándar (8 estaciones: A - H)")
    opcion = input("Selecciona la red a cargar (1 o 2): ").strip()

    if opcion == "2":
        return red_8, "Red de Prueba (8 estaciones)"
    return red_12, "Red Propia (12 estaciones)"


def main():
    grafo, nombre_red = seleccionar_red()
    print(f"\nCargada: {nombre_red}")
    print("Estaciones disponibles:", ", ".join(grafo.keys()))
    print("\nLista de adyacencia:")
    for estacion, vecinos in grafo.items():
        print(f"  {estacion} -> {', '.join(vecinos)}")

    while True:
        print("\n----------------------------------------------")
        inicio = input("Estación de inicio (o 'SALIR' para terminar): ").strip().upper()
        if inicio == "SALIR":
            break

        destino = input("Estación de destino: ").strip().upper()

        if inicio not in grafo or destino not in grafo:
            print("Error: Una o ambas estaciones no existen en esta red.")
            continue

        ruta_bfs = buscar_bfs(grafo, inicio, destino)
        ruta_dfs = buscar_dfs(grafo, inicio, destino)

        print("\n--- Resultados de Búsqueda ---")
        if ruta_bfs:
            print(f"BFS (Menor número de paradas): {' -> '.join(ruta_bfs)} ({len(ruta_bfs) - 1} saltos)")
        else:
            print("BFS: No se encontró ruta.")

        if ruta_dfs:
            print(f"DFS (Exploración en profundidad): {' -> '.join(ruta_dfs)} ({len(ruta_dfs) - 1} saltos)")
        else:
            print("DFS: No se encontró ruta.")

if __name__ == "__main__":
    main()