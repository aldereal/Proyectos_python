import math

def es_primo(numero):
    # contador = 0

    # for i in range(1, numero + 1):
    #     if i == 1 or i == numero:
    #         continue
    #     if numero % i == 0:
    #         contador += 1
    # if contador == 0:
    #     return True
    # else:
    #     return False

    # contador = 0

    # for i in range(1, int(math.sqrt(numero) + 1)):
    #     if i == 1 or i == numero:
    #         continue
    #     if numero % i == 0:
    #         contador += 1
    # if contador == 0:
    #     return True
    # else:
    #     return False


def run():
    # numero = int(input('Escribe un número y te diré si es primo: '))
    # # if numero != 2 and numero % 2 == 0:
    # #     print('No es primo')
    # # else:
    # #     if es_primo(numero):
    # #         print('Es primo')
    # #     else:
    # #         print('No es primo') 

    numero = int(input('Digita un número: '))
    contador = 2
    primo = True
    while contador < numero:
        if numero % contador == 0:
            print('Es primo')
            primo = False
            break
        else:
            contador += 1
    if primo == True:
        print('El número es primo')


if __name__ == '__main__':
    run()