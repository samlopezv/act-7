def main():
    #escribe tu código abajo de esta línea
    x = int(input('Dame un lado: '))
    y = int(input('Dame un lado: '))
    z = int(input('Dame un lado: '))

    if (x > 0 and y > 0 and z > 0) and (x+y>z and x+z>y and y+z>x) :

        if x == y == z :
            print ('Triángulo equilátero')

        elif (x == y and y!= z ) or (x ==z and z!=y) or (y==z and z!= x):
            print ('Trángulo isóceles')

        else:
            print ('Triángulo escaleno')
    
    else:
        print('Estas medidas no son de un trángulo')

    

if __name__=='__main__':
    main()
