if __name__ == "__main__":


    parola = input("Inserisci una parola da trasformare con il Burrows-Wheeler: ")

    arrParola = list(parola)
    copiaArr = arrParola
    arrFinale = []
    copiaArr.append("$")

    for i in range(0, len(copiaArr)):
        arrFinale.append("".join(copiaArr))
        copiaArr.insert(len(copiaArr), copiaArr[0])
        copiaArr.pop(0)
        

    print(arrFinale)
    arrFinale.sort()
    
    print(arrFinale)

