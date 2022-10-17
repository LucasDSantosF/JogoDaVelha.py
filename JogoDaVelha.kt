val matrix = mutableListOf<MutableList<String>>()

fun matrixStructure() {
    matrix.add(mutableListOf(" ", " ", " "))
    matrix.add(mutableListOf(" ", " ", " "))
    matrix.add(mutableListOf(" ", " ", " "))
}

fun verifyMatrixIndex(result: List<Int>): List<Int> {
    var result1 = result
    while (0 > result1[0] || result1[0] > 2 && 0 > result1[1] || result1[1] > 2) {
        println("Um dos valores informados está fora dos limites do jogo. Por favor digite novamente.")
        result1 = getLineAndColumn()
    }
    return result1
}

fun addItem(item: String, list: List<Int>) {
    var list1 = verifyMatrixIndex(list)
    while (matrix[list1[0]][list1[1]] != " ") {
        println("Essa pocição ja contem um valor. Por favor digite de novo.")
        list1 = verifyMatrixIndex(getLineAndColumn())
    }
    matrix[list1[0]][list1[1]] = item
}

fun getLineAndColumn(): List<Int> {
    print("Linha: ")
    var p1 = readLine().orEmpty()
    print("Coluna: ")
    var p2 = readLine().orEmpty()
    println()
    while ((p1 in "123").not() && (p2 in "123").not()) {
        println(
            "Um dos valores informados nao eh um um numero ou" +
                    "\nUm dos valores informados esta fora dos limites do jogo. Por favor digite novamente."
        )
        print("Linha: ")
        p1 = readLine().orEmpty()
        print("Coluna: ")
        p2 = readLine().orEmpty()
        println()
    }
    return listOf(p1.toInt() - 1, p2.toInt() - 1)
}

fun verifyWinner(item: String): Int {
    var vezes = 0

    for (i in 0..2) {
        for (j in 0..2) {
            if (matrix[i][j] == item) {
                vezes += 1
            }
        }
        if (vezes == 3) break else vezes = 0
    }

    if (vezes == 3) return 1

    for (i in 0..2) {
        for (j in 0..2) {
            if (matrix[j][i] == item) {
                vezes += 1
            }
        }
        if (vezes == 3) break else vezes = 0
    }

    if (vezes == 3) return 1

    for (i in 0..2) {
        if (matrix[i][i] == item) {
            vezes += 1
        }
    }


    if (vezes == 3) return 1 else vezes = 0

    for (i in 0..2) {
        if (matrix[i][2 - i] == item) {
            vezes += 1
        }
    }

    if (vezes == 3) return 1

    return 0
}

fun showWinner(num: Int){
    showMatrix()
    println("Jogador ${num} Ganhou !!!")
}

fun game() {
    var quant = 0
    var count = 1
    matrixStructure()
    while (quant != 9) {
        showMatrix()
        val result = getLineAndColumn()

        when (count % 2) {
            1 -> {
                addItem(item = "O", list = result)
                count += 1
                if (verifyWinner("O") == 1){
                    showWinner(num = 1)
                    break
                }
            }
            else -> {
                addItem(item = "X", list = result)
                count += 1
                if (verifyWinner("X") == 1){
                    showWinner(num = 2)
                    break
                }
            }
        }
        quant += 1
    }
    if (quant == 9) {
        showMatrix()
        println("Deu velha kkkkkkk")
    }
}

fun showMatrix() {
    print("~-~-~-~-~-~-~-~\n\t")
    for (r in 0..2) {
        print("  ${r + 1}")
    }
    println()

    for (i in 0..2) {
        print("${i + 1} - ")
        for (j in 0..2) {
            print("  ${matrix[i][j]}")
        }
        println()
    }
    println("~-~-~-~-~-~-~-~")
}

fun main() {
    game()
}