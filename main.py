def trasformata_bwt(parola: str):
    arrParola = list(parola)
    arrFinale = []
    arrParola.append("$")

    for i in range(0, len(arrParola)):
        arrFinale.append(arrParola.copy())
        arrParola.insert(len(arrParola), arrParola[0])
        arrParola.pop(0)
        
    print("\nrotazione parola: ")
    print(arrFinale)
    parola = parola + "$"
    rotazioni = []

    
    for i in range(len(parola)):
        rotazioni.append(parola[i:] + parola[:i])

    n = len(rotazioni)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if rotazioni[j] > rotazioni[j + 1]:
                temp = rotazioni[j]
                rotazioni[j] = rotazioni[j + 1]
                rotazioni[j + 1] = temp

    
    risultato = ""
    for r in rotazioni:
        risultato = risultato + r[-1]

    print("\nrotazioni ordinate: ")
    print(arrFinale)

    risultato = ""

    for j in range(len(arrFinale)):
        risultato = risultato + arrFinale[j][len(arrParola)-1]

    print("\nrisultato della trasformazione BWT: ")
    print(risultato)
    return risultato



if __name__ == "__main__":
    parola = input("Inserisci una parola da trasformare con il Burrows-Wheeler: ")
    trasformata_bwt(parola)