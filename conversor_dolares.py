def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuántos pesos " + tipo_pesos + " tienes?:"))
    dolares = pesos / valor_dolar
    dolares = str(round(dolares, 2))
    print("Tienes $ " + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 😊

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Eligue una opción: """

opcion = int(input(menu))

if opcion == 1: 
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingresa una opción correcta, perro")

