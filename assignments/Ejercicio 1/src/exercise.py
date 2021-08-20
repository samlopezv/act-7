def main():
    #escribe tu código abajo de esta línea
    n = int(input('Dame un número: '))

    if n >= 0:
        if n%2 ==0:
            print('Positivo par')
        else :
            print('Positivo impar')

    else:
        if n%2 ==0:
            print('Negativo par')
        else:
            print ('Negativo impar')

if __name__=='__main__':
    main()
