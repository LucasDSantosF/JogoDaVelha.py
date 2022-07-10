matrix = [["", "", ""]["", "", ""]["", "", ""]]

def ShowMatrix(matrix):
    print("~-"*10+'\n'+'    ', end='')

    for r in range(0, 3):
        print(f' {r+1} ', end='')

    print()

    for i in range(0, 3):
        print(f"{i+1} - ", end='')
        for j in range(0, 3):
            print(f" {matrix[i][j]} ", end='')
        print('\n')

    print("~-"*10)

def Game():
    count = 1
    qunat = 0

    ShowMatrix(matrix = matrix)

    p1 = int(input("linha: ")) - 1
    p2 = int(input("Coluna: ")) - 1
    qunat += 1


