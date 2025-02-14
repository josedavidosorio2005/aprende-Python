#Juego de ahorcado

import random
import os

def limpiar_pantalla():
    # Limpiar pantalla en Windows o Unix
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_palabra():
    palabras = [
        "python", "programacion", "computadora", "tecnologia", "desarrollo",
        "videojuego", "internet", "software", "aplicacion", "variable",
        "funcion", "clase", "objeto", "matriz", "bucle"
    ]
    return random.choice(palabras).upper()

def mostrar_ahorcado(intentos):
    etapas = [
        # Estado final: perdió
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # 1 intento restante
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        # 2 intentos restantes
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        # 3 intentos restantes
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        # 4 intentos restantes
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        # 5 intentos restantes
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        # 6 intentos restantes
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """,
        # Estado inicial
        """
           --------
           |
           |
           |
           |
           |
           -
        """
    ]
    return etapas[intentos]

def jugar_ahorcado():
    palabra = obtener_palabra()
    letras_por_adivinar = set(palabra)  # conjunto de letras en la palabra
    letras_adivinadas = set()  # conjunto de letras adivinadas
    abecedario = set('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
    
    intentos = 7  # número de intentos permitidos

    # Bucle principal del juego
    while len(letras_por_adivinar) > 0 and intentos > 0:
        limpiar_pantalla()
        print("\n¡JUEGO DEL AHORCADO!\n")
        print(mostrar_ahorcado(intentos))
        
        # Mostrar letras usadas
        print("\nLetras usadas:", ' '.join(sorted(letras_adivinadas)))

        # Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '_' for letra in palabra]
        print("\nPalabra:", ' '.join(palabra_lista))
        
        # Obtener la letra del jugador
        letra = input("\nIngresa una letra: ").upper()
        
        # Validar la entrada
        if letra not in abecedario:
            print("\n¡Por favor, ingresa una letra válida!")
            input("\nPresiona Enter para continuar...")
            continue
        if letra in letras_adivinadas:
            print("\n¡Ya usaste esa letra!")
            input("\nPresiona Enter para continuar...")
            continue

        # Añadir la letra a las letras adivinadas
        letras_adivinadas.add(letra)
        
        # Verificar si la letra está en la palabra
        if letra in letras_por_adivinar:
            letras_por_adivinar.remove(letra)
            print("\n¡Bien hecho! La letra está en la palabra")
        else:
            intentos -= 1
            print("\n¡Oh no! La letra no está en la palabra")
            if intentos == 0:
                limpiar_pantalla()
                print(mostrar_ahorcado(0))
                print(f"\n¡Perdiste! La palabra era: {palabra}")
                break

        input("\nPresiona Enter para continuar...")

    # Si se adivinó la palabra
    if len(letras_por_adivinar) == 0:
        limpiar_pantalla()
        print(f"\n¡Felicitaciones! ¡Adivinaste la palabra {palabra}!")

def main():
    while True:
        jugar_ahorcado()
        if input("\n¿Quieres jugar de nuevo? (S/N): ").upper() != 'S':
            break
    print("\n¡Gracias por jugar!")

if __name__ == "__main__":
    main()