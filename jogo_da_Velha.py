matriz = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def imprimir(matriz):
    print("~-"*10)
    print('    ', end='')
    for r in range(0, 3):
        print(f' {r+1} ', end='')
    print()
    for i in range(0, 3):
        print(f"{i+1} - ", end='')
        for j in range(0, 3):
            print(f" {matriz[i][j]} ", end='')
        print('')
    print("~-"*10)

cont = 1
quant = 0
while True:

    imprimir(matriz)

    p1 = int(input("linha: "))
    p2 = int(input("Coluna: "))
    quant += 1
    p1 = p1-1
    p2 = p2-1

    # trecho 2

    if cont%2 == 1:
        matriz[p1][p2] = 'O'
        cont += 1


        vezes = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if matriz[i][j] == "O":
                    vezes += 1
            if vezes == 3:
                break
            vezes = 0
        
        if vezes == 3:
            imprimir(matriz)
            print("Jogador 1 Galhou !!!")
            break

        vezes = 0        
        for i in range(0, 3):
            for j in range(0, 3):
                if matriz[j][i] == "O":
                    vezes += 1
            if vezes == 3:
                break
            vezes = 0
        
        if vezes == 3:
            imprimir(matriz)
            print("Jogador 1 Galhou !!!")
            break

        achou = True
        for i in range(0, 3):
            if matriz[i][i] != "O":
                achou = False
        
        if achou:
            imprimir(matriz)
            print("Jogador 1 Galhou !!!")
            break

        achou = True

        for i in range(0, 3):
            if matriz[i][3-i -1] != "O":
                achou = False
        
        if achou:
            imprimir(matriz)
            print("Jogador 1 Galhou !!!")
            break


    else:
        matriz[p1][p2] = "X"
        cont += 1
        vezes = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if matriz[i][j] == "X":
                    vezes += 1
            if vezes == 3:
                break
            vezes = 0

        if vezes == 3:
            imprimir(matriz)
            print("Jogador 2 Galhou !!!")
            break
        vezes = 0
        
        for i in range(0, 3):
            for j in range(0, 3):
                if matriz[j][i] == "X":
                    vezes += 1
            if vezes == 3:
                break
            vezes = 0

        if vezes == 3:
            imprimir(matriz)
            print("Jogador 2 Galhou !!!")
            break

        achou = True
        for i in range(0, 3):
            if matriz[i][i] != "X":
                achou = False
        
        if achou:
            imprimir(matriz)
            print("Jogador 2 Galhou !!!")
            break


        achou = True

        for i in range(0, 3):
            if matriz[i][3-i -1] != "X":
                achou = False
        
        if achou:
            imprimir(matriz)
            print("Jogador 2 Galhou !!!")
            break

    if quant == 9:
        imprimir(matriz)
        break   
    



    