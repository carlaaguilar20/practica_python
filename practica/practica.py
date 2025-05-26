import random

def jugar():
    # Generar número secreto
    numero_secreto = random.randint(1, 40)
    intentos = 0
    max_intentos = 5

    # Mensaje de bienvenida
    print("\n🎮 ADIVINA EL NÚMERO 🤯")
    print("- El número se encuentra entre 1 y 40")
    print("- Tienes cinco (5) intentos")
    print("- ¡Suerte!\n")

    while intentos < max_intentos:
        # Mostrar pistas en los intentos 4 y 5
        if intentos == 3:
            rango_min = max( 1, numero_secreto - 3)
            rango_max = min( 40, numero_secreto + 3)
            print(f"💡 Pista: el número secreto está entre {rango_min} y {rango_max}.")
        elif intentos == 4:
            rango_min = max( 1, numero_secreto - 2)
            rango_max = min( 40,numero_secreto + 2)
            print(f"💡 Pista: ¡Último intento! El número está entre {rango_min} y {rango_max}.")

        # Solicitar número al usuario
        try:
            intento = int(input(f"Intento {intentos + 1} de {max_intentos} - Adivina el número (entre 1 y 40): "))
        except ValueError:
            print("❌ Por favor ingresa un número válido.")
            continue

        if intento < 1 or intento > 40:
            print("❌ Número fuera de rango. Debe estar entre 1 y 40.")
            continue

        intentos += 1

        if intento == numero_secreto:
            print("🎉 ¡Felicidades! Has adivinado el número secreto.")
            break
        elif intento < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

    if intento != numero_secreto:
        print(f"😢 Lo siento, has perdido. El número secreto era {numero_secreto}.")

# Bucle principal para volver a jugar
while True:
    jugar()
    respuesta = input("\n¿Deseas jugar otra vez? (sí/no): ").strip().lower()
    if respuesta not in ['sí', 'si', 's']:
        print("👋 ¡Adiós! Gracias por jugar.")
        break
