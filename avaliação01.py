class ArrayList:
    def __init__(self):
        self.LEN = 5
        self.arrayList = [None] * self.LEN
        self.insertPosition = 0
        
    def insert(self, data):
        if self.isMemoryFull():
            self.increaseMemory()

        self.arrayList[self.insertPosition] = data
        self.insertPosition += 1     

    def insertAt(self, data, position):
        if position < 0 or position > self.insertPosition:
            print("Posição inválida")
            return

        if self.isMemoryFull():
            self.increaseMemory()

        for i in range(self.insertPosition, position, -1):  
            self.arrayList[i] = self.arrayList[i - 1]

        self.arrayList[position] = data
        self.insertPosition += 1

    def removeAt(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida")
            return

        data = self.arrayList[position]

        for i in range(position, self.insertPosition - 1):
            self.arrayList[i] = self.arrayList[i + 1]

        self.insertPosition -= 1
        self.arrayList[self.insertPosition] = None

        return data

    def remove(self):
        if self.isEmpty():
            print("A lista está vazia")
            return

        self.insertPosition -= 1

        data = self.arrayList[self.insertPosition]
        self.arrayList[self.insertPosition] = None

        return data

    def isEmpty(self):
        return self.insertPosition == 0
        
    def isMemoryFull(self):
        return self.insertPosition == len(self.arrayList)

    def increaseMemory(self):
        newArray = [None] * (2 * len(self.arrayList))

        self.copyElements(newArray, self.arrayList)

        self.arrayList = newArray
        newArray = None

    def copyElements(self, newArray, oldArray):
        for position in range(len(oldArray)):
            newArray[position] = oldArray[position]           

    def print(self):
        if self.isEmpty():
            print("Nenhum Planeta cadastrado")
            return

        for position in range(self.insertPosition):
            print(position, "-", self.arrayList[position])

array = ArrayList()

option = -1

while option != 0:

    print()
    print("LISTA DE PLANETAS")
    print()
    print("1 - Adicionar planeta")
    print("2 - Adicionar planeta em uma posição")
    print("3 - Remover último planeta")
    print("4 - Remover planeta por posição")
    print("5 - Mostrar planetas")
    print("0 - Sair")
    print()

    option = int(input("Escolha uma opção: "))

    if option == 1:
        nome = input("Nome do planeta: ")
        tipo = input("Tipo do planeta: ")

        planeta = nome + " - " + tipo

        array.insert(planeta)

        print("Planeta adicionado")

    elif option == 2:
        nome = input("Nome do planeta: ")
        tipo = input("Tipo do planeta: ")

        planeta = nome + " - " + tipo
        position = int(input("Digite a posição: "))

        array.insertAt(planeta, position)

    elif option == 3:
        planeta = array.remove()

        if planeta != None:
            print("Planeta removido:", planeta)

    elif option == 4:
        array.print()

        if array.isEmpty() == False:
            position = int(input("Digite a posição que deseja remover: "))

            planeta = array.removeAt(position)

            if planeta != None:
                print("Planeta removido:", planeta)

    elif option == 5:
        print()
        print("PLANETAS CADASTRADOS")
        array.print()

    elif option == 0:
        print("Programa encerrado")

    else:
        print("Opção inválida")