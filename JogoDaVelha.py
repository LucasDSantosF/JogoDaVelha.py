matrix = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

def ShowMatrix(matrix):
    print("~-"*10+'\n'+'    ', end='')

    for r in range(0, 3):
        print(f'  {r+1}', end='')

    print()

    for i in range(0, 3):
        print(f"{i+1} - ", end='')
        for j in range(0, 3):
            print(f"  {matrix[i][j]}", end='')
        print('\n')

    print("~-"*10)

def Add(item, p1 , p2):
    while matrix[p1][p2] != " ":
        print("Essa Pocição já contem um valor, Por favor digite de novo.")
        p1 = int(input("linha: ")) - 1
        p2 = int(input("Coluna: ")) - 1

    matrix[p1][p2] = item

def Verify(item) -> int:

    vezes = 0  
    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[i][j] == item:
                vezes += 1
        if vezes == 3:
            break
        vezes = 0
    
    if vezes == 3:
        return  1

    vezes = 0        
    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[j][i] == item:
                vezes += 1
        if vezes == 3:
            break
        vezes = 0

    if vezes == 3:
        return  1
    
    achou = True
    for i in range(0, 3):
        if matrix[i][i] != item:
            achou = False
    
    if achou:
        return  1

    achou = True
    for i in range(0, 3):
        if matrix[i][3-i -1] != item:
            achou = False
    
    if achou:
        return  1
    
    return 0 

def ShowWinner(num):
    ShowMatrix(matrix)
    print(f"Jogador {num} Ganhou !!!")

def Game():
    quant = 0
    count = 1
    while quant != 9:
        ShowMatrix(matrix = matrix)
        p1 = int(input("linha: ")) - 1
        p2 = int(input("Coluna: ")) - 1

        if count%2 == 1:
            Add(item= "O", p1=p1, p2=p2)
            count +=1
            isWinner = Verify(item= "O")
            if isWinner == 1:
                ShowWinner(1)
                break
        else:
            Add(item= "X", p1=p1, p2=p2)
            count +=1
            isWinner = Verify(item="X")
            if isWinner == 1:
                ShowWinner(2)
                break
            
        quant += 1

Game()