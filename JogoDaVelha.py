from typing import List
from unicodedata import numeric

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

def GetLineAndColumn() -> List:
        p1 = str(input("linha: "))
        p2 = str(input("Coluna: "))
        while(p1.isnumeric() == False and p2.isnumeric() == False):
            print("Um dos valores informados não é um um número. Por favor digite novamente.\n")
            p1 = str(input("linha: "))
            p2 = str(input("Coluna: ")) 
    
        return [int(numeric(p1)-1), int(numeric(p2)-1)]

def VerifyMatrixIndex(result) -> List:
    while(0>result[0] or result[0]>2 and 0>result[1] or result[1]>2):
        print("Um dos valores informados está fora dos limites do jogo. Por favor digite novamente.\n")
        result = GetLineAndColumn()
    
    return result


def Add(item, result=[]):
    result = VerifyMatrixIndex(result)
    while matrix[result[0]][result[1]] != " ":
        print("Essa Pocição já contem um valor. Por favor digite de novo.")
        result = VerifyMatrixIndex(GetLineAndColumn())


    matrix[result[0]][result[1]] = item

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
    result = []
    while quant != 9:
        ShowMatrix(matrix = matrix)
        result = GetLineAndColumn()
        p1 = result[0]
        p2 = result[1]

        if count%2 == 1:
            Add(item= "O", result=[p1, p2])
            count +=1
            isWinner = Verify(item= "O")
            if isWinner == 1:
                ShowWinner(1)
                break
        else:
            Add(item= "X", result=[p1, p2])
            count +=1
            isWinner = Verify(item="X")
            if isWinner == 1:
                ShowWinner(2)
                break
            
        quant += 1
    if (quant == 9):
        ShowMatrix(matrix)
        print("Deu velha kkkkkkk")

Game()